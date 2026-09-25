-- Keep generated print material inside the page without changing book source.

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

local function display_width_score(text)
  local compact = text:gsub('%s+', ' ')
  compact = compact:gsub('\\[A-Za-z]+', 'x')
  compact = compact:gsub('[{}]', '')
  return #compact
end

local MAX_DISPLAY_ROW_SCORE = 42
local INLINE_BREAK_SCORE = 28

local function protect_row_start(row)
  local whitespace, body = row:match('^(%s*)(.*)$')
  if body:sub(1, 1) == '[' then
    return whitespace .. '{}' .. body
  end
  return row
end

local function add_break(breaks, left, right)
  if left < 1 or right > left + 1 then return end
  local previous = breaks[#breaks]
  if previous and previous.left == left and previous.right == right then return end
  breaks[#breaks + 1] = {left = left, right = right}
end

local function collect_breaks(text, max_container_depth, include_commas, allow_ampersand)
  local brace_depth = 0
  local paren_depth = 0
  local bracket_depth = 0
  local sized_depth = 0
  local environment_depth = 0
  local breaks = {}
  local position = 1
  while position <= #text do
    local character = text:sub(position, position)
    if not escaped(text, position)
        and text:sub(position, position + 6) == [[\begin{]] then
      local environment_end = text:find('}', position + 7, true)
      if not environment_end then return nil end
      environment_depth = environment_depth + 1
      position = environment_end
    elseif not escaped(text, position)
        and text:sub(position, position + 4) == [[\end{]] then
      local environment_end = text:find('}', position + 5, true)
      if not environment_end then return nil end
      environment_depth = environment_depth - 1
      if environment_depth < 0 then return nil end
      position = environment_end
    elseif environment_depth > 0 then
      -- Nested alignment and matrix syntax is opaque to the outer wrapper.
    elseif text:sub(position, position + 1) == [[\\]]
        and brace_depth == 0 and sized_depth == 0
        and paren_depth == 0 and bracket_depth == 0 then
      return nil
    elseif not escaped(text, position)
        and text:sub(position, position + 4) == [[\left]] then
      sized_depth = sized_depth + 1
    elseif not escaped(text, position)
        and text:sub(position, position + 5) == [[\right]] then
      sized_depth = sized_depth - 1
      if sized_depth < 0 then return nil end
    elseif not escaped(text, position) then
      if character == '{' then
        brace_depth = brace_depth + 1
      elseif character == '}' then
        brace_depth = brace_depth - 1
        if brace_depth < 0 then return nil end
      elseif character == '(' then
        paren_depth = paren_depth + 1
      elseif character == ')' then
        paren_depth = paren_depth - 1
        if paren_depth < 0 then return nil end
      elseif character == '[' then
        bracket_depth = bracket_depth + 1
      elseif character == ']' then
        bracket_depth = bracket_depth - 1
        if bracket_depth < 0 then return nil end
      elseif (character == '&' and not allow_ampersand) or character == '%' then
        return nil
      elseif brace_depth == 0 and sized_depth == 0
          and paren_depth + bracket_depth <= max_container_depth then
        local spacing_end = nil
        for _, command in ipairs({[[\qquad]], [[\quad]]}) do
          if text:sub(position, position + #command - 1) == command then
            spacing_end = position + #command - 1
            break
          end
        end
        if spacing_end then
          add_break(breaks, spacing_end, spacing_end + 1)
        elseif include_commas and (character == ',' or character == ';') then
          local ending = position
          local cursor = position + 1
          while text:sub(cursor, cursor):match('[ \t\r\n]') do
            cursor = cursor + 1
          end
          for _, command in ipairs({[[\qquad]], [[\quad]]}) do
            if text:sub(cursor, cursor + #command - 1) == command then
              ending = cursor + #command - 1
              break
            end
          end
          add_break(breaks, ending, ending + 1)
        elseif character == '+' then
          local previous = text:sub(1, position - 1):match('([^%s])%s*$')
          if previous and not ('^_={[(,+-'):find(previous, 1, true) then
            add_break(breaks, position - 1, position)
          end
        end
      end
    end
    position = position + 1
  end
  if brace_depth ~= 0 or paren_depth ~= 0 or bracket_depth ~= 0
      or sized_depth ~= 0 or environment_depth ~= 0 then return nil end
  return breaks
end

local function reflow_rows(text, breaks)
  if not breaks or #breaks == 0 then return nil end
  local atomic = {}
  local cursor = 1
  for _, boundary in ipairs(breaks) do
    atomic[#atomic + 1] = text:sub(cursor, boundary.left)
    cursor = boundary.right
  end
  atomic[#atomic + 1] = text:sub(cursor)

  local rows = {}
  local row = atomic[1]
  for index = 2, #atomic do
    local combined = row .. atomic[index]
    if display_width_score(combined) > MAX_DISPLAY_ROW_SCORE and row:match('%S') then
      rows[#rows + 1] = row
      row = atomic[index]
    else
      row = combined
    end
  end
  rows[#rows + 1] = row
  if #rows < 2 then return nil end
  return rows
end

local function merge_breaks(first, second)
  local merged = {}
  for _, boundary in ipairs(first or {}) do
    add_break(merged, boundary.left, boundary.right)
  end
  for _, boundary in ipairs(second or {}) do
    merged[#merged + 1] = boundary
  end
  table.sort(merged, function(left, right)
    if left.left == right.left then return left.right < right.right end
    return left.left < right.left
  end)
  local unique = {}
  for _, boundary in ipairs(merged) do
    add_break(unique, boundary.left, boundary.right)
  end
  return unique
end

local function structured_rows(text)
  local top_level = collect_breaks(text, 0, true, false)
  local rows = reflow_rows(text, top_level)
  if rows then
    local nested_additions = collect_breaks(text, 1, false, false)
    local refined = reflow_rows(text, merge_breaks(top_level, nested_additions))
    if refined then rows = refined end
  else
    rows = reflow_rows(text, collect_breaks(text, 1, true, false))
  end
  return rows
end

local function gathered_display(text)
  if display_width_score(text) <= MAX_DISPLAY_ROW_SCORE then return nil end
  local rows = structured_rows(text)
  if not rows then return nil end

  local pieces = {[[\begin{gathered}]], protect_row_start(rows[1])}
  for index = 2, #rows do
    pieces[#pieces + 1] = [[\\]]
    pieces[#pieces + 1] = protect_row_start(rows[index])
  end
  pieces[#pieces + 1] = [[\end{gathered}]]
  return table.concat(pieces)
end

local function wrap_invisible_delimiter_break(text)
  local outer_start, outer_end = text:find("\\left[", 1, true)
  if not outer_start then return nil end
  local first_start, first_end = text:find([[\right.]], outer_end + 1, true)
  if not first_start then return nil end
  local second_start, second_end = text:find([[\left.]], first_end + 1, true)
  if not second_start or text:sub(first_end + 1, second_start - 1):match('%S') then
    return nil
  end
  local close_start, close_end = text:find("\\right]", second_end + 1, true)
  if not close_start then return nil end
  local tail = text:sub(second_end + 1, close_start - 1)
  local spacing_start, spacing_end = tail:find([=[^%s*\hspace%{[^}]+%}]=])
  if spacing_start then
    tail = tail:sub(spacing_end + 1)
  end
  return text:sub(1, outer_end)
    .. [[\begin{gathered}]] .. text:sub(outer_end + 1, first_start - 1)
    .. [[\\\quad{}]] .. tail .. [[\end{gathered}]]
    .. text:sub(close_start, close_end) .. text:sub(close_end + 1)
end

local function wrap_sized_body(text)
  for _, delimiter in ipairs({
    {"\\left\\{", "\\right\\}"},
    {"\\left[", "\\right]"},
    {"\\left(", "\\right)"},
  }) do
    local start_at, left_end = text:find(delimiter[1], 1, true)
    if start_at then
      local right_start, right_end = text:find(delimiter[2], left_end + 1, true)
      if right_start then
        local body = text:sub(left_end + 1, right_start - 1)
        if display_width_score(body) > MAX_DISPLAY_ROW_SCORE then
          local rows = structured_rows(body)
          if rows then
            local pieces = {text:sub(1, left_end), [[\begin{gathered}]],
              protect_row_start(rows[1])}
            for index = 2, #rows do
              pieces[#pieces + 1] = [[\\]]
              pieces[#pieces + 1] = protect_row_start(rows[index])
            end
            pieces[#pieces + 1] = [[\end{gathered}]]
            pieces[#pieces + 1] = text:sub(right_start, right_end)
            pieces[#pieces + 1] = text:sub(right_end + 1)
            return table.concat(pieces)
          end
        end
      end
    end
  end
  return nil
end

local function inline_breaks(text)
  if display_width_score(text) <= INLINE_BREAK_SCORE then return nil end
  local breaks = collect_breaks(text, 0, true, false) or {}
  local brace_depth, paren_depth, bracket_depth = 0, 0, 0
  for position = 1, #text do
    local character = text:sub(position, position)
    if not escaped(text, position) then
      if character == '{' then brace_depth = brace_depth + 1
      elseif character == '}' then brace_depth = brace_depth - 1
      elseif brace_depth == 0 and character == '(' then
        if paren_depth == 0 and bracket_depth == 0
            and text:sub(position - 1, position - 1):match('%s')
            and text:sub(1, position - 1):match('([^%s])%s*$') == '}' then
          breaks[#breaks + 1] = {left = position - 1, right = position}
        end
        paren_depth = paren_depth + 1
      elseif brace_depth == 0 and character == ')' then
        paren_depth = paren_depth - 1
        if paren_depth == 0 and bracket_depth == 0
            and text:sub(position + 1):match('%S') then
          breaks[#breaks + 1] = {left = position, right = position + 1}
        end
      elseif brace_depth == 0 and character == '[' then bracket_depth = bracket_depth + 1
      elseif brace_depth == 0 and character == ']' then
        bracket_depth = bracket_depth - 1
        if bracket_depth == 0 and paren_depth == 0
            and text:sub(position + 1):match('%S') then
          breaks[#breaks + 1] = {left = position, right = position + 1}
        end
      elseif brace_depth == 0 and paren_depth == 0 and bracket_depth == 0
          and character == '=' and position > 1 then
        breaks[#breaks + 1] = {left = position - 1, right = position}
      end
    end
  end
  if brace_depth ~= 0 or paren_depth ~= 0 or bracket_depth ~= 0 or #breaks == 0 then
    return nil
  end
  table.sort(breaks, function(left, right) return left.left < right.left end)
  local pieces, cursor, last = {}, 1, 0
  for _, boundary in ipairs(breaks) do
    if boundary.left > last then
      pieces[#pieces + 1] = text:sub(cursor, boundary.left)
      pieces[#pieces + 1] = [[\allowbreak{}]]
      cursor = boundary.right
      last = boundary.left
    end
  end
  pieces[#pieces + 1] = text:sub(cursor)
  return table.concat(pieces)
end

local function split_explicit_rows(body)
  local rows = {}
  local cursor = 1
  while true do
    local start_at, end_at = body:find([[\\]], cursor, true)
    if not start_at then
      rows[#rows + 1] = body:sub(cursor)
      break
    end
    rows[#rows + 1] = body:sub(cursor, start_at - 1)
    cursor = end_at + 1
  end
  return rows
end

local function wrap_aligned_rows(text)
  local opening = [[\begin{aligned}]]
  local closing = [[\end{aligned}]]
  local start_at, open_end = text:find(opening, 1, true)
  local close_at, close_end = text:find(closing, 1, true)
  if not start_at or not close_at or close_at <= open_end then return nil end
  if text:sub(1, start_at - 1):match('%S')
      or text:sub(close_end + 1):match('%S') then return nil end
  local body = text:sub(open_end + 1, close_at - 1)
  if body:find([[\begin]], 1, true) or body:find([[\end]], 1, true) then return nil end

  local original_rows = split_explicit_rows(body)
  local output_rows = {}
  local changed = false
  for _, row in ipairs(original_rows) do
    local _, ampersands = row:gsub('&', '')
    local wrapped = nil
    if ampersands == 1 and display_width_score(row) > MAX_DISPLAY_ROW_SCORE then
      wrapped = reflow_rows(row, collect_breaks(row, 1, false, true))
    end
    if wrapped then
      output_rows[#output_rows + 1] = wrapped[1]
      for index = 2, #wrapped do
        output_rows[#output_rows + 1] = [[&\quad{}]] .. protect_row_start(wrapped[index])
      end
      changed = true
    else
      output_rows[#output_rows + 1] = row
    end
  end
  if not changed then return nil end
  return text:sub(1, open_end) .. table.concat(output_rows, [[\\]])
    .. text:sub(close_at)
end

local function compact_wide_array(text)
  if display_width_score(text) <= 60 then return nil end
  local specification = text:match([=[\begin%{array%}%{([^}]*)%}]=])
  if not specification then return nil end
  local _, columns = specification:gsub('[clrpmb]', '')
  if columns < 6 then return nil end
  return [[{\scriptsize ]] .. text .. [[}]]
end

function Math(math)
  if FORMAT ~= 'latex' then return nil end
  if math.mathtype == 'InlineMath' then
    local inline = inline_breaks(math.text)
    if not inline then return nil end
    math.text = inline
    return math
  end
  if math.mathtype ~= 'DisplayMath' then return nil end
  local replacement = compact_wide_array(math.text)
    or wrap_invisible_delimiter_break(math.text)
    or wrap_aligned_rows(math.text)
    or wrap_sized_body(math.text)
    or gathered_display(math.text)
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
