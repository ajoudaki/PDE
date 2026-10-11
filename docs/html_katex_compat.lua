-- KaTeX lacks mathtools' psmallmatrix environment. Preserve its small-matrix
-- layout and parentheses in HTML without changing the book's TeX sources.
function Math(el)
  if quarto.doc.is_format("html") then
    el.text = el.text
      :gsub("\\begin{psmallmatrix}", "\\left(\\begin{smallmatrix}")
      :gsub("\\end{psmallmatrix}", "\\end{smallmatrix}\\right)")
  end
  return el
end
