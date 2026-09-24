-- Bound Mermaid figures and use breakable blocks for two-column print tables.

function Image(image)
  if FORMAT == 'latex' and image.src:match('mermaid%-figure%-%d+%.png$') then
    image.attributes.width = nil
    image.attributes.height = nil
    return image
  end
end

local function escaped(text, position)
  local count = 0
  position = position - 1
  while position >= 1 and text:sub(position, position) == '\\' do
    count = count + 1
    position = position - 1
  end
  return count % 2 == 1
end

local function gathered_display(text)
  if text:find([[\\]], 1, true)
      or text:find([[\begin]], 1, true)
      or text:find([[\end]], 1, true)
      or text:find([[\left]], 1, true)
      or text:find([[\right]], 1, true) then
    return nil
  end

  local depth = 0
  local breaks = {}
  local position = 1
  while position <= #text do
    local character = text:sub(position, position)
    if not escaped(text, position) then
      if character == '{' then
        depth = depth + 1
      elseif character == '}' then
        depth = depth - 1
        if depth < 0 then return nil end
      elseif character == '&' or character == '%' then
        return nil
      elseif character == ',' and depth == 0 then
        local _, quad_end = text:find([[^,\quad]], position)
        if quad_end and text:find('^[ \t]*\r?\n', quad_end + 1) then
          breaks[#breaks + 1] = quad_end
        end
      end
    end
    position = position + 1
  end
  if depth ~= 0 or #breaks < 2 then return nil end

  local pieces = {[[\begin{gathered}]]}
  local cursor = 1
  for _, break_at in ipairs(breaks) do
    pieces[#pieces + 1] = text:sub(cursor, break_at)
    pieces[#pieces + 1] = [[\\]]
    cursor = break_at + 1
  end
  pieces[#pieces + 1] = text:sub(cursor)
  pieces[#pieces + 1] = [[\end{gathered}]]
  return table.concat(pieces)
end

function Math(math)
  if FORMAT ~= 'latex' or math.mathtype ~= 'DisplayMath' then return nil end
  local replacement = gathered_display(math.text)
  if not replacement then return nil end
  math.text = replacement
  return math
end

local function warn(reason)
  io.stderr:write('Breakable-table filter left a two-column print table unchanged: '
    .. reason .. '\n')
end

local function spans(cell)
  return (cell.row_span or 1) ~= 1 or (cell.col_span or 1) ~= 1
end

local function unsupported(table)
  if table.identifier ~= '' then return 'labelled table' end
  if (table.caption.long and #table.caption.long > 0)
      or (table.caption.short and #table.caption.short > 0) then
    return 'captioned table'
  end
  if #table.head.rows ~= 1 then return 'expected one header row' end
  if #table.bodies ~= 1 then return 'expected one table body' end
  if #table.foot.rows ~= 0 then return 'table foot is unsupported' end
  local body = table.bodies[1]
  if body.row_head_columns ~= 0 or #body.head ~= 0 then
    return 'row headers or intermediate headers are unsupported'
  end
  local columns = #table.head.rows[1].cells
  for _, row in ipairs(table.head.rows) do
    if row.identifier ~= '' then return 'labelled header row' end
    if #row.cells ~= columns then return 'inconsistent header width' end
    for _, cell in ipairs(row.cells) do
      if cell.identifier ~= '' then return 'labelled header cell' end
      if spans(cell) then return 'spanning header cell' end
    end
  end
  for _, row in ipairs(body.body) do
    if row.identifier ~= '' then return 'labelled body row' end
    if #row.cells ~= columns then return 'inconsistent row width' end
    for _, cell in ipairs(row.cells) do
      if cell.identifier ~= '' then return 'labelled body cell' end
      if spans(cell) then return 'spanning body cell' end
    end
  end
end

function Table(table)
  if FORMAT ~= 'latex' or #table.colspecs ~= 2 then return nil end
  local reason = unsupported(table)
  if reason then
    warn(reason)
    return nil
  end
  local blocks = pandoc.Blocks({})
  local headers = table.head.rows[1].cells
  for _, row in ipairs(table.bodies[1].body) do
    local fields = pandoc.Blocks({})
    for column, cell in ipairs(row.cells) do
      local label = pandoc.utils.blocks_to_inlines(headers[column].contents)
      fields:insert(pandoc.Para({pandoc.Strong(label)}))
      fields:extend(cell.contents)
    end
    blocks:insert(pandoc.Div(fields, pandoc.Attr('', {'pdf-table-row'})))
    blocks:insert(pandoc.HorizontalRule())
  end
  return pandoc.Div(blocks, table.attr)
end
