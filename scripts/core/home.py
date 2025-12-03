from scripts.constants import CONF, MOVE, WAIT
import scripts.core.battle as battle
import pyautogui as pg
import time
from config import IMAGES
from scripts.logger import log

logwin = None  # 由外部注入

def go_home(force=False):
    """
    回城流程。force=True 时直接执行回城，无需检测图片
    """
    while True:
        location = True if force else pg.locateOnScreen(IMAGES["home"], confidence=CONF["mid"], grayscale=True)
        if location:
            log("检测到需要回城，开始回城流程，等待动画结束")
            time.sleep(WAIT["home_pc"])

            battle.exit_battle()
            log("退出战斗")

            battle.down()
            battle.right()
            log("选择逃跑")

            battle.run()
            log("确认逃跑,等待逃跑动画结束")
            time.sleep(WAIT["home_ready"])
            log("逃跑成功，准备回城")

            battle.pc()
            log("回城中，等待瞬间移动回城动画结束")
            time.sleep(WAIT["home_start"])
            log("回城流程完成")

            log(f"对话护士{WAIT['home_conversation_start']}s，准备回复")
            battle.keydown_run()
            time.sleep(WAIT["home_conversation_start"])
            battle.keyup_run()
            time.sleep(WAIT["home_conversation_end"])

            log(f"向下移动角色{MOVE['keydown_down']}s，出pc")
            battle.keydown_down()
            time.sleep(MOVE["keydown_down"])
            battle.keyup_down()
            log("向下移动角色完成，等待出pc动画")
            time.sleep(WAIT["out_pc"])

            log("出pc完成，等待动画，准备骑车离开")
            time.sleep(WAIT["ready_bike"])
            battle.bike()
            log("骑车离开,加载骑车动画")
            time.sleep(WAIT["ready_bike"])


            log(f"向左移动角色{MOVE['keydown_left']}s，准备到水边")
            battle.keydown_left()
            time.sleep(MOVE["keydown_left"])
            battle.keyup_left()

            log(f"向下移动角色{MOVE['keydown_down_water']}s，到水边钓鱼")
            battle.keydown_down()
            time.sleep(MOVE["keydown_down_water"])
            battle.keyup_down()
            time.sleep(WAIT["ready_fish"])
            break
        log("pp充足")
        break