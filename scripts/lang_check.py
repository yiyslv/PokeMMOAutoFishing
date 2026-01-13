import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

import ctypes
import time
import cv2
import numpy as np
import pyautogui as pg
from config import IMAGES,DEBUG_PATH
from constants import CONF
from core.battle import keydown_ctrl, keyup_ctrl, space
from logger import log

user32 = ctypes.windll.user32
VK_CONTROL = 0x11
VK_SPACE   = 0x20

# 右下角附近 60×30 区域（自行微调 x, y, w, h）
ROI = (1685, 1040, 20, 20)
def _capture_roi():
    """返回 ROI 的 BGR 数组"""
    return np.array(pg.screenshot(region=ROI))

def _match_template(img, tpl_path):
    tpl = cv2.imread(tpl_path, cv2.IMREAD_COLOR)
    if tpl is None:
        return False
    h_img, w_img = img.shape[:CONF["roi"]]
    h_tpl, w_tpl = tpl.shape[:CONF["roi"]]
    # 模板太大就等比缩小到 ROI 的 80%
    if h_tpl > h_img or w_tpl > w_img:
        scale = min(h_img / h_tpl, w_img / w_tpl) * 0.8
        tpl = cv2.resize(tpl, (int(w_tpl * scale), int(h_tpl * scale)))
    res = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    return max_val > 0.8

def _send_ctrl_space():
    keydown_ctrl()
    space()
    keyup_ctrl()
    time.sleep(0.1)

def ensure_english_input_method(verbose=False):
    img = _capture_roi()
    is_zh = _match_template(img, IMAGES["zh"])
    is_en = _match_template(img, IMAGES["en"])

    if is_zh and not is_en:
        _send_ctrl_space()
        verbose = True
        if verbose:
            log("OCR 检测到中文图标，已 Ctrl+Space 切换为英文")
    else:
        if verbose:
            log("OCR 检测到英文图标，无需切换")

#"""
if __name__ == "__main__":
    ensure_english_input_method(verbose=True)

    roi_img = _capture_roi()
    save_path = DEBUG_PATH["debug_roi"] / "debug_roi.png"
    cv2.imwrite(str(save_path), roi_img)
    log(f"已保存当前 ROI 到 {save_path.resolve()}，请打开核对是否包含“中/英”图标")
#"""