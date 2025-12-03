# tools/remove_str_wrap.py
from pathlib import Path
import re

proj = Path(__file__).parent.parent
scripts = proj / "scripts"

for py in scripts.glob("*.py"):
    txt = orig = py.read_text(encoding="utf-8")

    # 1. 删除 str(IMAGES[...]) 包裹
    txt = re.sub(r'str\((IMAGES\["\w+"\])\)', r'\1', txt)
    # 2. 删除 .as_posix() 包裹
    txt = re.sub(r'(IMAGES\["\w+"\])\.as_posix\(\)', r'\1', txt)
    # 3. 删除 f"{IMAGES[...]}" 包裹
    txt = re.sub(r'f"(\{IMAGES\["\w+"\]\})"', r'\1', txt)

    if txt != orig:
        py.write_text(txt, encoding="utf-8")
        print(f"✅ {py.name}")