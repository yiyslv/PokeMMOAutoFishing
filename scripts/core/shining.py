import subprocess
import pyautogui as pg
import os
import time
from datetime import datetime
from config import IMAGES
from scripts.constants import CONF, COUNT, MAX, WAIT
from scripts.logger import log

logwin = None  # 由外部注入

def _capture_fullscreen():
    """返回全屏截图路径"""
    fname = f"shining_{datetime.now():%m%d_%H%M%S}.png"
    path = os.path.join(os.environ["TEMP"], fname)
    pg.screenshot(path)
    return path

def _wait_and_click(img):
    """等到图出现就点中心，超时放弃"""
    box = pg.locateOnScreen(img, confidence=CONF["low"], grayscale=True) # 低分辨率 my_computer
    if box:
        if img == IMAGES["my_computer"]:
            x_right = box.left + box.width + 100
            y_center = box.top + box.height // 2
            pg.click(x_right, y_center)
            pg.click(x_right, y_center)
        else:
            pg.click(pg.center(box))
        return True
    return False

def _send_qq_my_computer(img_path):
    # 1. 图片进剪贴板
    subprocess.run(["powershell", "-command", f"Set-Clipboard -Path '{img_path}'"], check=True)
    time.sleep(WAIT["base"])

    # 2. 点击任务栏 QQ 图标（唤出主面板）
    if not _wait_and_click(IMAGES["qq_taskbar"]):
        log("没找到 QQ 任务栏图标，放弃发送")
        return
    time.sleep(WAIT["qq_taskbar"])          # 等主面板完全弹出

    # 3. 双击「我的电脑」联系人（永远在顶部）
    if not _wait_and_click(IMAGES["my_computer"]):
        log("没找到『我的电脑』联系人，放弃发送")
        return
    time.sleep(WAIT["my_computer"])            # 等聊天窗口加载

    # 4. 粘贴 + 发送
    pg.hotkey('ctrl', 'v')   # 粘贴截图
    time.sleep(WAIT["qq_send"])          # 留足上传
    if not _wait_and_click(IMAGES["qq_send"]):
        log("没找到发送按钮，放弃发送")
        return
    log("已发送截图到 QQ 我的电脑")
def check_shining():
    """检测到闪光→截图→发 QQ→退出"""
    for _ in range(MAX["shining"]):
        if pg.locateOnScreen(IMAGES["shining"], confidence=CONF["mid"], grayscale=True): # 中分辨率 shining
            log("检测到闪光，准备截图并发 QQ")
            COUNT['count_shining'] += 1
            log(f"本次闪光次数: {COUNT['count_shining']} 次")
            if logwin:
                log("检测到闪光，正在截图并发往 QQ「我的手机」")

            # 1. 全屏截图
            pic = _capture_fullscreen()
            log(f"截图已保存: {pic}")

            # 2. 发送到 QQ「我的手机」
            _send_qq_my_computer(pic)

            # 3. 日志 & 退出
            if logwin:
                log("截图已发送，准备终止脚本")
            time.sleep(WAIT["all_stop"])
            os._exit(0)          # 强制退出整个进程
        time.sleep(WAIT["base"])