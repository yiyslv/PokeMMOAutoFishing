import pydirectinput as pd
import time
from constants import KEYS,WAIT
from scripts.logger import log
def run():
    """
    执行一次战斗操作：
    按下 'z' 键（通常为攻击或确认），等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['attack']}键，确认/攻击")
    pd.press(KEYS["attack"])      # 按下攻击键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def fish():
    """
    执行一次钓鱼操作：
    按下 '5' 键（通常为钓鱼），等待WAIT["base"]秒
    """
    log(f"按下 5 键，钓鱼")
    pd.press('5')      # 按下钓鱼键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def pc():
    """
    执行一次瞬间移动操作：
    按下 '6' 键（通常为瞬间移动），等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['pc']}键，使用瞬间移动")
    pd.press(KEYS["pc"])      # 按下 瞬间移动 键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def bike():
    """
    执行一次骑车操作：
    按下 '1' 键（通常为骑车），等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['bike']}键，骑车")
    pd.press(KEYS["bike"])      # 按下骑车键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def down():
    """
    执行一次向下移动操作：
    按下 'KEYS["down"]' 键（通常为向下移动），等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['down']}键，向下移动")
    pd.press(KEYS["down"])      # 按下向下移动键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def right():
    """
    执行一次向右移动操作：
    按下 'KEYS["right"]' 键（通常为向右移动），等待WAIT["base"]秒
    """ 
    log(f"按下 {KEYS['right']}键，向右移动")
    pd.press(KEYS["right"])      # 按下向右移动键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def exit_battle():
    """
    执行一次退出战斗操作：
    按下 'KEYS["exit_battle"]' 键（通常为退出战斗），等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['exit_battle']}键，退出战斗")
    pd.press(KEYS["exit_battle"])      # 按下KEYS["exit_battle"]键
    time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keydown_down():
    """
    按下KEYS["down"]键，等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['down']}键，开始向下移动")
    pd.keyDown(KEYS["down"])      # 按下 KEYS["down"] 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keyup_down():
    """
    抬起KEYS["down"]键，等待WAIT["base"]秒
    """
    log(f"抬起 {KEYS['down']} 键，停止向下移动")
    pd.keyUp(KEYS["down"])      # 抬起 KEYS["down"] 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keydown_run():
    """
    按下KEYS["attack"]键，等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['attack']}键，开始")
    pd.keyDown(KEYS["attack"])      # 按下 KEYS["attack"]键 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keyup_run():
    """
    抬起KEYS["attack"]键，等待WAIT["base"]秒
    """
    log(f"抬起 {KEYS['attack']} 键，停止")
    pd.keyUp(KEYS["attack"])      # 抬起 KEYS["attack"]键 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keydown_left():
    """
    按下KEYS["left"]键，等待WAIT["base"]秒
    """
    log(f"按下 {KEYS['left']} 键，开始向左移动")
    pd.keyDown(KEYS["left"])      # 按下 KEYS["left"] 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快

def keyup_left():
    """
    抬起KEYS["left"]键，等待WAIT["base"]秒
    """
    log(f"抬起 {KEYS['left']} 键，停止向左移动")
    pd.keyUp(KEYS["left"])      # 抬起 KEYS["left"] 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快


def keydown_ctrl():
    """
    按下 Ctrl 键，等待WAIT["base"]秒
    """
    log("按下 Ctrl 键")
    pd.keyDown('ctrl')      # 按下 Ctrl 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快
def keyup_ctrl():
    """
    抬起 Ctrl 键，等待WAIT["base"]秒
    """
    log("抬起 Ctrl 键")
    pd.keyUp('ctrl')      # 抬起 Ctrl 键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快
def space():
    """
    按下空格键，等待WAIT["base"]秒
    """
    log("点按 空格键")
    pd.press('space')      # 点按 空格键
    #time.sleep(WAIT["base"])    # 等待WAIT["base"]秒，防止操作过快