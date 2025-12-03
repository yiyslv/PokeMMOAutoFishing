import os
import pyautogui as pg
from enum import Enum
from typing import Optional
from config import IMAGES
from scripts.constants import CONF
from scripts.logger import log


logwin = None  # 由外部注入

# 定义游戏状态枚举
class State(Enum):
    WALKING = 1
    BATTLING = 2
    FREEZE = 3
    SHINING = 4
    HOME = 5
    CONTINUE = 6
    FISH_SUCCESS = 7
    FISH_FAIL = 8

# 玩家角色图片列表，用于判断是否行走状态
imageRefs = [IMAGES["player_left"], IMAGES["player_right"]]


def _locate_image(img_path: str, confidence: float = CONF["high"], grayscale: bool = True) -> Optional[object]:
    """
    封装的 locateOnScreen，先检查文件存在，捕获读取异常并记录日志。
    返回 pyautogui.locateOnScreen 的结果或 None。
    """
    if not os.path.exists(img_path):
        # 记录但不抛出，避免因为单张图片缺失导致脚本崩溃
        try:
            logwin.log(f"图片未找到: {img_path}")
        except Exception:
            pass
        return None

    try:
        return pg.locateOnScreen(img_path, confidence=confidence, grayscale=grayscale)
    except OSError as e:
        try:
            log(f"读取图片失败: {img_path} -> {e}")
        except Exception:
            pass
        return None
    except Exception as e:
        try:
            log(f"检测图片时发生异常: {img_path} -> {e}")
        except Exception:
            pass
        return None

def check_walk_state_indicator() -> Optional[State]:
    """
    检查屏幕上是否有玩家角色图片。
    返回 State.WALKING 或 None（未识别/战斗中由外部判断）。
    """
    player_imgs = []
    for imageRef in imageRefs:
        loc = _locate_image(imageRef, confidence=CONF["high"])
        player_imgs.append(loc)
    # 若至少识别到一个玩家头像则认为处于行走状态
    if player_imgs.count(None) < len(imageRefs):
        log("检测到玩家角色图片，处于行走状态")  
        return State.WALKING       
    log("未检测到玩家角色图片，可能处于战斗中或其他状态")
    return None

def check_battle_state_indicator() -> Optional[State]:
    """
    检查是否处于战斗界面（通过战斗指示图片）。
    返回 State.BATTLING 或 None。
    """
    if _locate_image(IMAGES["battle_state"]):
        log("检测到战斗状态指示图片，处于战斗状态")
        return State.BATTLING
    log("未检测到战斗状态指示图片")
    return None

def check_freeze_state_indicator() -> Optional[State]:
    """
    检查是否处于冻结状态。
    返回 State.FREEZE 或 None。
    """
    if _locate_image(IMAGES["freeze"]):
        log("检测到冻结状态指示图片，处于冻结状态")
        return State.FREEZE
    log("未检测到冻结状态指示图片")
    return None

def check_shining_state_indicator() -> Optional[State]:
    """
    检查是否处于闪光（稀有）状态。
    返回 State.SHINING 或 None。
    """
    if _locate_image(IMAGES["shining"]):
        log("检测到闪光状态指示图片，处于闪光状态")
        return State.SHINING
    log("未检测到闪光状态指示图片")
    return None

def check_home_state_indicator() -> Optional[State]:
    """
    检查是否出现回城提示。
    返回 State.HOME 或 None。
    """
    if _locate_image(IMAGES["home"]):
        log("检测到回城状态指示图片，处于回城状态")
        return State.HOME
    log("未检测到回城状态指示图片")
    return None

def check_continue_state_indicator() -> Optional[State]:
    """
    检查是否出现“继续/战斗未结束”提示。
    返回 State.CONTINUE 或 None。
    """
    if _locate_image(IMAGES["continue"]):
        log("检测到继续状态指示图片，处于继续状态")
        return State.CONTINUE
    log("未检测到继续状态指示图片")
    return None

def check_fish_success_state_indicator() -> Optional[State]:
    """
    检查钓鱼是否成功。
    返回 State.FISH_SUCCESS 或 None。
    """
    if _locate_image(IMAGES["fish_success"]):
        log("检测到钓鱼成功状态指示图片，钓鱼成功")
        return State.FISH_SUCCESS
    log("未检测到钓鱼成功状态指示图片")
    return None

def check_fish_fail_state_indicator() -> Optional[State]:
    """
    检查钓鱼是否失败。
    返回 State.FISH_FAIL 或 None。
    """
    if _locate_image(IMAGES["fish_fail"]):
        log("检测到钓鱼失败状态指示图片，钓鱼失败")
        return State.FISH_FAIL
    log("未检测到钓鱼失败状态指示图片")
    return None