# scripts/logger.py  2025-06-25  统一日志入口
import sys
from typing import Optional

_logwin: Optional[object] = None

def set_logwin(logwin_obj):
    """由 main.py 在启动后调用一次即可"""
    global _logwin
    _logwin = logwin_obj

def log(msg: str, *, also_print: bool = True):
    """一条日志同时走控制台 + 日志窗口"""
    if also_print:
        print(msg)
    if _logwin is not None:
        try:
            _logwin.log(msg)
        except Exception:
            print("【日志窗口写入失败】", msg, file=sys.stderr)