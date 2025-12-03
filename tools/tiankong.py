import pydirectinput as pd
import time

def repeat_tab_and_ctrl_v(times, delay=0.1):
    for _ in range(times):
        pd.press('tab')
        time.sleep(delay)
        pd.keyDown('ctrl')
        pd.press('v')
        pd.keyUp('ctrl')
        time.sleep(delay)

if __name__ == "__main__":
    repeat_tab_and_ctrl_v(70)  # 重复