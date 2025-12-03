import time
import pyautogui as pg

print("3 秒后把鼠标移到“中/英”图标左上角，停住 1 秒…")
time.sleep(3)
x1, y1 = pg.position()
print("再移到图标右下角，停住 1 秒…")
time.sleep(3)
x2, y2 = pg.position()
w, h = x2 - x1, y2 - y1
print(f"ROI = ({x1}, {y1}, {w}, {h})")
# 顺手截一张当前小图，当模板
#pg.screenshot("images/zh_roi.png", region=(x1, y1, w, h))
#print("已保存模板 images/zh_roi.png，可直接用")