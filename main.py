import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# ---------- 一次性导入 ----------
from scripts.logger import log, set_logwin   # 新增 set_logwin
import scripts.state as state
import scripts.core.home as home
import scripts.core.freeze as freeze
import scripts.core.shining as shining
import scripts.core.continueBattle as continueBattle
import scripts.core.fishing as fishing
from scripts.ui.log_window import get_logwin
from scripts.lang_check import ensure_english_input_method

ensure_english_input_method()

# ---------- 注入 ----------
logwin = get_logwin()
for m in (state, home, freeze, shining, continueBattle, fishing):
    m.logwin = logwin

# ---------- 启动 ----------
if __name__ == "__main__":
    logwin = get_logwin()
    logwin.start_background(force_thread=True)
    set_logwin(logwin)          # 必须先注入
    log("日志窗口已请求启动")    # 第一行日志

    # 现在再开始监听键盘/循环/OCR
    try:
        fishing.fish()          # 里面才会监听 Ctrl/空格
    except Exception as e:
        log(f"主逻辑异常: {e}")
        raise