import time
import pyautogui as pg
from scripts.constants import CONF, MAX, WAIT
from scripts.core import home
from scripts.core import battle, freeze
from config import IMAGES
from scripts.logger import log

logwin = None  # 由外部注入
def continueBattle(success: bool = False):
    success = False
    countBattle = 1
    for _ in range(MAX["continue"]):
        if pg.locateOnScreen(IMAGES["continue"], confidence=CONF["high"], grayscale=True):
            success = True
            run()
            countBattle += 1
            log(f"继续战斗，第 {countBattle} 回合战斗结束")
            return success
        else:
            log("结束，继续钓鱼")
            return success

def run():
    log("未结束，继续战斗")
    freeze.check_freeze() # 隐藏检测freeze
    battle.run()
    log("选择战斗")
    battle.run()
    log("攻击")
    home.go_home() # 检测pp
    time.sleep(WAIT["attack"])
    log("等待加载战斗动画")