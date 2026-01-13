import time
import pyautogui as pg
from scripts.constants import CONF, MAX, WAIT, COUNT
from scripts.core import home, shining
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
    if freeze.check_freeze(): # 隐藏检测freeze
        return
    battle.run()
    log("选择战斗")
    battle.run()
    log("攻击")
    if home.go_home():       # PP 不足回城
        COUNT['count_battle_fail'] += 1
        COUNT['count_home'] += 1
        return
    time.sleep(WAIT["attack"])
    log("等待加载战斗动画")

def firstBattle():
        time.sleep(WAIT["fish_success"]) # 等待钓鱼成功动画结束
        battle.run()           # 确认进入战斗
        log("加载战斗动画")
        time.sleep(WAIT["fish_attack_start"]) # 等待战斗动画加载

        shining.check_shining()  # 检测到会退出脚本

        battle.run()             # 选择战斗
        battle.run()             # 攻击
        if home.go_home():       # PP 不足回城
            COUNT["count_battle_fail"] += 1
            COUNT["count_home"] += 1
            return

        log("等待战斗动画结束")
        time.sleep(WAIT["fish_attack_end"])  # 等待战斗动画结束
        log("第1回合战斗结束")
        if freeze.check_freeze():
            COUNT["count_freeze"] += 1
            COUNT["count_home"] += 1
            COUNT["count_battle_fail"] += 1
            return

def Attack():
    firstBattle()    
    if continueBattle():
        COUNT["count_continue"] += 1
    else:
        COUNT["count_perfect"] += 1
