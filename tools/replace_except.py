import re
from pathlib import Path

for py in Path("scripts").glob("*.py"):
    txt = orig = py.read_text(encoding="utf-8")
    # 把 except Exception as e: logwin.log(f"..." 替换
    txt = re.sub(
        r'except Exception.*?as\s+\w+:\s*\n\s*logwin\.log\(f?"([^"]+)"\s*\+?\s*\w*\)',
        'except Exception:\n        log_stack("\\1")',
        txt,
        flags=re.S
    )
    if 'log_stack' in txt and 'from scripts.utils import log_stack' not in txt:
        txt = 'from scripts.utils import log_stack\n' + txt
    if txt != orig:
        py.write_text(txt, encoding="utf-8")
        print(f"✅ {py.name}")