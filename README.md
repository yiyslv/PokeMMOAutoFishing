## 项目简介

PokeMMOAutoFishing 是一款基于图像模板匹配与模拟按键的**宝可梦自动钓鱼脚本**。  
通过 OpenCV 识别游戏画面中的状态图标，自动完成「钓鱼 → 战斗 → 回城治疗 → 继续钓鱼」循环，并支持：

- 闪光（异色）告警 + 自动截图发送 QQ
- 冻结/ PP 不足 / 连续战斗 等多种异常处理
- 实时日志悬浮窗，方便调试与状态监控
- 输入法自动切换（中→英），避免指令失效

> 仅支持 **Windows 10/11** 简体中文版，**1920×1080 分辨率** 下测试通过。  
> 观众多开源项目有感，开发此项目仅供学习研究，禁止用于商业及破坏游戏公平性场景。

> assets\images 里面的图片可能根据游戏版本不同有差异，可替换（可参照对比 scripts\config.py 第7行IMAGES）
> scripts\lang_check.py 第20行ROI = (1685, 1040, 20, 20)是为了鼠标点击更改中英文如有需要根据分辨率和位置修改（若无合适像素计算方法可参考 tools\test_location.py 计算）
> scripts/constants.py 41行KEYS键位可修改
> 如果性能，延迟不同可微调 scripts/constants.py 参数 
> 只对涟漪湾的钓鱼点做了持续优化，其他位置不可行

---

## 功能特性

| 模块         | 描述                                                     |
| ------------ | -------------------------------------------------------- |
| `fishing`    | 自动抛竿、识别钓鱼成功/失败、进入战斗                    |
| `battle`     | 自动按 `z` 攻击；支持连续战斗检测                        |
| `home`       | PP 不足或强制回城时，自动瞬移→治疗→骑车→返回水边         |
| `freeze`     | 被冰冻时瞬移回城                                         |
| `shining`    | 出现闪光宝可梦 → 全屏截图 → 发送到「我的电脑」→ 退出脚本 |
| `lang_check` | 检测输入法，中文时 `Ctrl+Space` 切回英文                 |
| `log_window` | 半透明置顶日志悬浮窗，可拖拽、支持点击穿透               |

---

## 运行环境

- Windows 10/11（**DPI 100%**）

- Python 3.9 ~ 3.11 64-bit，实验环境为3.10.6

- 1920×1080 分辨率，游戏窗口**必须位于主屏幕**

- 游戏内需要设置的**快捷键**：

  - `z` 攻击 / 确认
  - `x` 退出战斗
  - `1` 骑车
  - `5` 钓鱼
  - `6` 瞬间移动
  - 方向键移动

- \-自行激活虚拟环境执行或在项目根目录下执行：

  ```
  .venv\Scripts\python.exe main.py
  ```

- -需要打开qq并有显示在任务栏并将**我的手机**（或自行修改）置顶以便出闪时发消息提醒

- \- 喵喵最好满级

- \- 自行研究

------

## 使用（Windows）

1.项目根目录创建并激活虚拟环境（推荐） 

```
python -m venv .venv 
.venv\Scripts\activate
```

2.安装依赖 

```
pip install -r requirements.txt
```

3.将「assets/images」里的模板图替换为你自己的游戏实测截图（保留同名即可，先执行根据需求修改即可）

4.运行脚本 

```
python main.py 
```

若看到半透明黑色日志窗口弹出，即表示启动成功；3秒内立即切换回游戏窗口，脚本将自动开始钓鱼。

---

## 项目结构

**PokeMMOAutoFishing 项目结构**

```
PokeMMOAutoFishing/                 # 项目根目录
│
├── main.py                         # 入口脚本
├── requirements.txt                # Python 依赖清单
├── README.md                       # 项目说明
├── .gitignore                      # Git 忽略规则
├── assets/                         # 静态资源
│   ├── images/                     # 模板截图（钓鱼/战斗/异常等）
│   └── debug_path/                 # 调试 ROI 输出
│
├── scripts/                        # 核心代码
│   ├── core/                       # 业务逻辑模块
│   │   ├── battle.py               # 战斗/按键封装
│   │   ├── fishing.py              # 钓鱼主循环
│   │   ├── home.py                 # 回城治疗流程
│   │   ├── freeze.py               # 冻结检测
│   │   ├── shining.py              # 闪光检测+QQ截图
│   │   └── continueBattle.py       # 连续战斗
│   │
│   ├── ui/
│   │   └── log_window.py           # 悬浮日志窗
│   │
│   ├── config.py                   # 路径与模板图配置
│   ├── constants.py                # 置信度/等待时间/按键常量
│   ├── lang_check.py               # 输入法切换
│   ├── logger.py                   # 统一日志
│   └── state.py                    # 游戏状态检测
│
├── tools/                          # 开发辅助
│   └── test_location.py            # 截图/坐标调试脚本
│
└── .venv/                          # 虚拟环境（Windows）
```

