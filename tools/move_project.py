# tools/move_project.py
import shutil
from pathlib import Path

root = Path(__file__).parent.parent
scripts = root / "scripts"

# 1. 创建新文件夹
(scripts / "core").mkdir(exist_ok=True)
(scripts / "ui").mkdir(exist_ok=True)
(scripts / "capture").mkdir(exist_ok=True)
(root / "assets" / "images").mkdir(parents=True, exist_ok=True)
(root / "tools").mkdir(exist_ok=True)
(root / "tests").mkdir(exist_ok=True)

# 2. 核心模块搬家
core_files = ["battle.py", "fishing.py", "continueBattle.py",
              "home.py", "freeze.py", "shining.py"]
for f in core_files:
    if (scripts / f).exists():
        shutil.move(scripts / f, scripts / "core" / f)

# 3. UI 模块搬家
ui_files = ["log_window.py"]
for f in ui_files:
    if (scripts / f).exists():
        shutil.move(scripts / f, scripts / "ui" / f)

# 4. 图片搬家
if (root / "images").exists():
    shutil.move(root / "images", root / "assets" / "images")

print("✅ 搬仓完成，请按新结构更新 .gitignore 与 README")