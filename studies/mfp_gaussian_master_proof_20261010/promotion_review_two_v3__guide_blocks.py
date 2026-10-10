"""Execute every Python-fenced MFP guide block in its own namespace."""
from pathlib import Path
import re

blocks = re.findall(r'```python\n(.*?)\n```', Path('code/MFP_CALCULUS.md').read_text(), re.S)
for number, block in enumerate(blocks, 1):
    print(f'GUIDE PYTHON BLOCK {number}')
    exec(compile(block, f'MFP_CALCULUS.md:block{number}', 'exec'), {})
print(f'ALL {len(blocks)} PYTHON GUIDE BLOCKS PASSED')
