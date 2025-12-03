import re
from pathlib import Path

# 映射表：旧数字 → 新常量
MAGIC_MAP = [
    (r'\b0\.95\b', 'CONF_HIGH'),
    (r'\b0\.9\b', 'CONF_MID'),
    (r'\b0\.8\b', 'CONF_LOW'),
    (r'\b10\b', 'WAIT_BATTLE_ANIM'),
    (r'\b2\b', 'WAIT_MID'),          # 注意：可能误伤，先全局扫一眼
    (r'\b5\b', 'MAX_FREEZE_CHECK'),
    (r'\b1\b', 'WAIT_MID'),          # 同样先确认
]

for py in Path("scripts").glob("*.py"):
    txt = orig = py.read_text(encoding="utf-8")
    for old, new in MAGIC_MAP:
        txt = re.sub(old, new, txt)

    # 自动加导入（若还没有）
    if any(v in txt for v in {'CONF_HIGH', 'WAIT_MID', 'MAX_FREEZE_CHECK'}):
        if 'from scripts.constants import' not in txt:
            txt = 'from scripts.constants import CONF_HIGH, CONF_MID, CONF_LOW, WAIT_MID, WAIT_BATTLE_ANIM, MAX_FREEZE_CHECK\n' + txt

    if txt != orig:
        py.write_text(txt, encoding="utf-8")
        print(f"✅ {py.name}")