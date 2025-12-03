import pyautogui as pg
import time
from scripts.constants import CONF, MAX, WAIT
import scripts.core.home as home
from config import IMAGES
from scripts.logger import log

logwin = None  # 由外部注入

def check_freeze():
    """
    检查屏幕是否出现freeze图片，最多检测5次，出现则直接回城（不再检测home图片）
    """
    for _ in range(MAX["freeze"]):
        location = pg.locateOnScreen(IMAGES["freeze"], confidence=CONF["high"], grayscale=True)
        if location:
            log("被冻结，直接回城")
            home.go_home(force=True)
            break
        time.sleep(WAIT["check_freeze"])