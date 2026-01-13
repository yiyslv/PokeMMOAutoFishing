from scripts import state
#import pydirectinput as pd
import time
import pyautogui as pg
from scripts.constants import CONF, MAX, WAIT, COUNT
from scripts.core import battle, continueBattle, freeze, home, shining
from scripts.lang_check import ensure_english_input_method
from config import IMAGES
from scripts.logger import log, msg

logwin = None   # 由外部注入


# ------------------------------------------------------------------
# ① 提取重复代码：统一处理所有异常状态
# ------------------------------------------------------------------
def handle_exceptional_states() -> bool:
    """
    检测到任何“非钓鱼”状态就处理并返回 True，让外层直接 continue；
    无任何异常则返回 False，继续正常流程。
    """
    if state.check_shining_state_indicator() == state.State.SHINING:
        shining.check_shining()          # 内部会退出脚本
        return True                      # 保险起见
    if state.check_freeze_state_indicator() == state.State.FREEZE:
        log("被冻结，直接回城")
        home.go_home(force=True)
        return True
    if state.check_home_state_indicator() == state.State.HOME:
        log("检测到pp不足，执行回城流程")
        home.go_home()
        return True
    if state.check_battle_state_indicator() == state.State.BATTLING:
        log("进入战斗，继续战斗")
        continueBattle.continueBattle()
        return True
    if state.check_continue_state_indicator() == state.State.CONTINUE:
        log("继续，继续战斗")
        continueBattle.continueBattle()
        return True
    if state.check_fish_success_state_indicator() == state.State.FISH_SUCCESS:
        log("钓鱼成功，准备进入战斗")
        return True
    if state.check_fish_fail_state_indicator() == state.State.FISH_FAIL:
        log("钓鱼失败，准备重新钓鱼")
        battle.run()
        return True
    return False


# ------------------------------------------------------------------
# ② 主流程
# ------------------------------------------------------------------
def fish():
    ensure_english_input_method()

    # 启动前统一检查一次
    handle_exceptional_states()

    while True:
        ensure_english_input_method()
        battle.fish()
        COUNT["count_all"] += 1
        log(f"开始第 {COUNT['count_all']} 次钓鱼")

        time.sleep(WAIT["fish_start"])          # 等钓鱼动画

        # ----------------------------------------------------------
        # ③ 钓鱼结果判定
        # ----------------------------------------------------------
        success = fail = False
        for _ in range(MAX["fishing"]):
            if pg.locateOnScreen(IMAGES["fish_success"], confidence=CONF["high"], grayscale=True):
                success, fail = True, False
                COUNT["count_fish"] += 1
                log("钓鱼成功，进入战斗")
                break
            if pg.locateOnScreen(IMAGES["fish_fail"], confidence=CONF["high"], grayscale=True):
                fail, success = True, False
                log("钓鱼失败，重新钓鱼")
                break
            time.sleep(WAIT["base"])

        if fail:
            time.sleep(WAIT["fish_fail"])      # 等钓鱼失败动画
            battle.run()
            COUNT["count_fail"] += 1
            log("本次钓鱼失败")
            msg()
            continue

        if not success:        # 什么都没检测到
            log("未检测到钓鱼结果,出错，重试整个流程")
            handle_exceptional_states()   # 统一处理
            continue

        # ----------------------------------------------------------
        # ④ 成功钓鱼 → 进入战斗流程
        # ----------------------------------------------------------
        continueBattle.Attack()

        # ----------------------------------------------------------
        # ④ 流程结束 → 统计日志
        # ----------------------------------------------------------
        log("本次钓鱼完成")
        msg()