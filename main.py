import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# 只写一次导入（全部放在这里）
from scripts.logger import log
import scripts.state as state
import scripts.core.home as home
import scripts.core.freeze as freeze
import scripts.core.shining as shining
import scripts.core.continueBattle as continueBattle
import scripts.core.fishing as fishing
from scripts.ui.log_window import get_logwin
from scripts.lang_check import ensure_english_input_method

ensure_english_input_method()   # 只有中文才切换输入法

# 统一注入（只写一次）
logwin = get_logwin()
for m in (state, home, freeze, shining, continueBattle, fishing):
    m.logwin = logwin

if __name__ == "__main__":
    logwin.start_background(force_thread=True)
    log("日志窗口已请求启动")
    try:
        fishing.fish()
    except Exception as e:
        log(f"主逻辑异常: {e}")
        raise