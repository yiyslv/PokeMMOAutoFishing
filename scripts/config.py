#from scripts.constants import CONF_HIGH, CONF_MID, CONF_LOW, WAIT_MID, WAIT_BATTLE_ANIM, MAX_FREEZE_CHECK
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # 指向项目根目录
IMG_DIR  = BASE_DIR / "assets"

IMAGES = {
    # 钓鱼
    "fish_success": IMG_DIR / "images/fish_success.png",
    "fish_fail":    IMG_DIR / "images/fish_fail.png",

    # 战斗
    "battle_state": IMG_DIR / "images/battle_state_indicator.png",
    "continue":     IMG_DIR / "images/continue.png",

    # 异常
    "freeze":       IMG_DIR / "images/freeze.png",
    "shining":      IMG_DIR / "images/shining.png",
    "home":         IMG_DIR / "images/home.png",

    # 玩家朝向
    "player_left":  IMG_DIR / "images/player_faceleft.png",
    "player_right": IMG_DIR / "images/player_faceright.png",

    # QQ 截图
    "qq_taskbar":   IMG_DIR / "images/qq_taskbar.png",
    "my_computer":  IMG_DIR / "images/my_computer.png",
    "qq_send":      IMG_DIR / "images/qq_send.png",

    # 输入法
    "zh":           IMG_DIR / "images/zh.png",
    "en":           IMG_DIR / "images/en.png",
}

# 自动把所有 Path 对象转成字符串，外部零改动
IMAGES = {k: str(v) for k, v in IMAGES.items()}

DEBUG_PATH= {
    "debug_roi": IMG_DIR / "debug_path/"
}