# tools/bulk_replace_img_path.py  一次性脚本
import re
from pathlib import Path

PROJ   = Path(__file__).parent.parent
SCRIPT = PROJ / "scripts"

# ① 需要替换的映射表
MAP = {
    r'"images/fish_success\.png"' : 'IMAGES["fish_success"]',
    r'"images/fish_fail\.png"'    : 'IMAGES["fish_fail"]',
    r'"images/battle_state_indicator\.png"' : 'IMAGES["battle_state"]',
    r'"images/continue\.png"'     : 'IMAGES["continue"]',
    r'"images/freeze\.png"'       : 'IMAGES["freeze"]',
    r'"images/shining\.png"'      : 'IMAGES["shining"]',
    r'"images/home\.png"'         : 'IMAGES["home"]',
    r'"images/player_faceleft\.png"' : 'IMAGES["player_left"]',
    r'"images/player_faceright\.png"': 'IMAGES["player_right"]',
    r'"images/qq_taskbar\.png"'   : 'IMAGES["qq_taskbar"]',
    r'"images/my_computer\.png"'  : 'IMAGES["my_computer"]',
    r'"images/qq_send\.png"'      : 'IMAGES["qq_send"]',
    r'"images/zh\.png"'           : 'IMAGES["zh"]',
    r'"images/en\.png"'           : 'IMAGES["en"]',
}

for py in SCRIPT.glob("*.py"):
    txt = orig = py.read_text(encoding="utf-8")

    # ② 替换路径
    for old, new in MAP.items():
        txt = re.sub(old, new, txt)

    # ③ 自动加导入（若还没有）
    if 'IMAGES[' in txt and 'from scripts.config import IMAGES' not in txt:
        txt = 'from scripts.config import IMAGES\n' + txt

    # ④ 写回
    if txt != orig:
        py.write_text(txt, encoding="utf-8")
        print(f"✅ {py.name}")