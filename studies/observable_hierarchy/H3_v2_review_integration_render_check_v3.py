from pathlib import Path
import hashlib
import json
import markdown

root = Path.cwd()
scratch = Path(__file__).resolve().parent
source = root / 'review/proposed_section.md'
line = source.read_text().splitlines()[838]
rendered = markdown.markdown(line)
assert '<a href="(1+s)epsilon_N+tau(s)">C(1+s)T</a>' in rendered
result = {'source': str(source), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'source_line': 839, 'frozen_chapter_line': 13393,
          'input': line, 'rendered_html': rendered, 'markdown_version': markdown.__version__,
          'finding': 'The second factor in the inequality is consumed as a link destination.'}
(scratch / 'render_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
