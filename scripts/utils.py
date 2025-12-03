# scripts/utils.py  2025-06-25  统一记录异常堆栈
import traceback
from scripts.logger import log

def log_stack(msg: str, also_print: bool = True):
    """记录自定义消息 + 当前堆栈"""
    stack = traceback.format_exc()
    if stack and stack != "NoneType: None\n":
        log(f"{msg}\n{stack}", also_print=also_print)
    else:
        log(msg, also_print=also_print)