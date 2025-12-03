# tools/replace_log.py
import re
from pathlib import Path

proj = Path(__file__).parent.parent
scripts = proj / "scripts"

for py in scripts.glob("*.py"):
    txt = orig = py.read_text(encoding="utf-8")

    # 1. 删除旧的双行日志
    txt = re.sub(r'print\("([^"]+)"\)\s*\n\s*logwin\.log\(\1\)', r'log("\1")', txt)
    # 2. 单行 print 转 log
    txt = re.sub(r'print\("([^"]+)"\)', r'log("\1")', txt)
    # 3. 已有 logwin.log 转 log
    txt = re.sub(r'logwin\.log\("([^"]+)"\)', r'log("\1")', txt)

    # 4. 自动加导入（若还没有）
    if 'log("' in txt and 'from scripts.logger import log' not in txt:
        txt = 'from scripts.logger import log\n' + txt

    if txt != orig:
        py.write_text(txt, encoding="utf-8")
        print(f"✅ {py.name}")