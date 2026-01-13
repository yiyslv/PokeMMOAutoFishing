# scripts/logger.py  2025-12-07  调试版
import sys
from typing import Optional

from constants import COUNT

_logwin: Optional[object] = None

def set_logwin(logwin_obj):
    """由 main.py 在启动后调用一次即可"""
    global _logwin
    _logwin = logwin_obj
    print(f"[LOGGER] set_logwin() called, object={logwin_obj}")

# scripts/logger.py
_early_logs = []

def log(msg: str, *, also_print=True):
    if also_print:
        print(msg)

    if _logwin is None:                 # 窗口还没好
        _early_logs.append(msg)
        return

    for m in _early_logs:               # 补写缓存
        try:
            _logwin.log(m)
        except Exception:
            pass
    _early_logs.clear()

    try:
        _logwin.log(msg)
    except Exception as e:
        print('【日志窗口写入失败】', msg, e, file=sys.stderr)

def msg():                              #统计日志
        log("当前统计: "
        f"总钓鱼: all={COUNT['count_all']}, 钓鱼成功: fish={COUNT['count_fish']}, "
        f"完美钓鱼: perfect={COUNT['count_perfect']}, 继续战斗: continue={COUNT['count_continue']}, "
        f"钓鱼失败: fail={COUNT['count_fail']}, 冻结: freeze={COUNT['count_freeze']}, "
        f"未完战斗: battle_fail={COUNT['count_battle_fail']}, 回城: home={COUNT['count_home']}, "
        f"闪光: shining={COUNT['count_shining']}")