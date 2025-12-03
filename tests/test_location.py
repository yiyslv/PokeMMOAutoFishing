from scripts.constants import CONF_HIGH, CONF_MID, CONF_LOW, WAIT_MID, WAIT_BATTLE_ANIM, MAX_FREEZE_CHECK
from scripts.logger import log
import time
import pyautogui as pg

log("3 秒后把鼠标移到“中/英”图标左上角，停住 WAIT_MID 秒…")
time.sleep(3)
x1, y1 = pg.position()
log("再移到图标右下角，停住 WAIT_MID 秒…")
time.sleep(3)
x2, y2 = pg.position()
w, h = x2 - x1, y2 - y1
print(f"ROI = ({x1}, {y1}, {w}, {h})")
# 顺手截一张当前小图，当模板
#pg.screenshot("images/zh_roi.png", region=(x1, y1, w, h))
#log("已保存模板 images/zh_roi.png，可直接用")