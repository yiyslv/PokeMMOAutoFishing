# scripts/constants.py  2025-06-25  魔法数字总入口

# ---------- 图像识别 ----------
CONF={
    "high":0.95, # 高分辨率 
    "mid":0.90, # 中分辨率 shining/pp
    "low":0.80, # 低分辨率 my_computer
    "start": 0,
    "roi": 2
}

# ---------- 等待时间（秒） ----------
WAIT={
    "base": 0.5,
    "qq_taskbar": 1.5, # 检测QQ任务栏
    "my_computer": 2, # 检测QQ窗口加载
    "qq_send": 1.5, # 检测截图上传
    "all_stop": 1, # 检测所有停止
    "attack": 10, #等待战斗画面

    "home_pc": 2, # 检测PC
    "home_ready": 5, # 等待逃跑动画结束
    "home_start": 6, # 等待瞬间移动回城动画结束
    "home_conversation_start": 11, # 对话护士时间
    "home_conversation_end": 1, # 对话结束
    "out_pc": 1, # 等待出pc动画
    "ready_bike": 1, # 等待准备骑车动画
    "ready_fish": 1, # 等待准备钓鱼动画

    "check_freeze": 1, # 检测是否冻结
    "check_shining": 1, # 检测是否闪    

    "fish_start": 2, # 等待钓鱼动画
    "fish_fail": 1, # 等待钓鱼失败动画
    "fish_success": 1, # 等待钓鱼成功动画
    "fish_attack_start": 10, # 等待战斗动画加载
    "fish_attack_end": 13, # 等待战斗动画结束
}

# ---------- 按键 ----------
KEYS={
    "attack": "z", # 确认键
    "bike": "1", # 骑行键
    "pc": "6",  # 瞬间移动键
    "exit_battle": "x", # 退出战斗键
    "down": "down", # 移动键
    "left": "left", # 移动键
    "right": "right", # 移动键
    "up": "up", # 移动键
}

# ---------- 移动时间（秒） ----------
MOVE={
    "keydown_down": 2.8, # 向下移动角色    
    "keydown_left": 0.65, # 向左移动角色
    "keydown_down_water": 1.3, # 向下移动角色到水边
}

# ---------- 检测次数 ----------
MAX={
    "freeze": 3, # 检测是否冻结
    "shining": 6, # 检测是否闪
    "fishing": 5, # 检测钓鱼结果
    "continue": 5 # 连续战斗次数
}

# ---------- 计数器 ----------
COUNT={
    "count_fish": 0,
    "count_freeze": 0,
    "count_continue": 0,
    "count_shining": 0,
    "count_home": 0,
    "count_fail": 0,
    "count_perfect": 0,
    "count_all": 0,
    "count_battle_fail": 0
}