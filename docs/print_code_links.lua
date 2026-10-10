-- Keep local code-resource URLs inside the PDF/LaTeX export directory.
function Link(link)
  if FORMAT:match('latex') and link.target:match('^%.%./code/') then
    link.target = link.target:sub(4)
    return link
  end
end
