from __future__ import annotations
from typing import Optional
import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import multiprocessing as mp
import ctypes
import time
import threading

from scripts.logger import log

def _apply_windows_window_style_hwnd(hwnd: int, no_activate: bool = True, enable_transparent: bool = False):
    try:
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x00080000
        WS_EX_TRANSPARENT = 0x00000020
        WS_EX_TOOLWINDOW = 0x00000080
        WS_EX_NOACTIVATE = 0x08000000
        user32 = ctypes.windll.user32
        style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        new_style = style | WS_EX_LAYERED | WS_EX_TOOLWINDOW
        if no_activate:
            new_style |= WS_EX_NOACTIVATE
        if enable_transparent:
            new_style |= WS_EX_TRANSPARENT
        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)
        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        SWP_NOACTIVATE = 0x0010
        HWND_TOPMOST = -1
        user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0,
                            SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)
    except Exception:
        pass

def _log_window_server(queue: mp.Queue, width: int = 480, height: int = 220, opacity: float = 0.88):
    try:
        open(os.path.join(os.path.dirname(__file__), "log_window_child_started.txt"), "w").write("started\n")
    except Exception:
        pass

    try:
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        try:
            root.attributes("-alpha", opacity)
        except Exception:
            pass

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        x = (screen_w - width) // 2
        y = screen_h - height - 48
        root.geometry(f"{width}x{height}+{x}+{y}")

        bg, fg, title_bg = "#111216", "#e6eef6", "#0f1720"

        title = tk.Frame(root, bg=title_bg, height=28)
        title.pack(fill=tk.X, side=tk.TOP)
        tk.Label(title, text="日志窗口", bg=title_bg, fg=fg, padx=8).pack(side=tk.LEFT, padx=(6, 0))

        body = tk.Frame(root, bg=bg)
        body.pack(fill=tk.BOTH, expand=True)
        font = tkfont.Font(family="Consolas", size=11)
        text = tk.Text(body, bg=bg, fg=fg, insertbackground=fg, font=font,
                       wrap=tk.WORD, padx=6, pady=6, bd=0)
        text.config(state=tk.DISABLED)
        vsb = ttk.Scrollbar(body, orient=tk.VERTICAL, command=text.yview)
        text['yscrollcommand'] = vsb.set
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 拖动
        _drag = {"x": 0, "y": 0}
        def _on_drag_start(e):
            _drag["x"], _drag["y"] = e.x, e.y
        def _on_drag_motion(e):
            root.geometry(f"+{root.winfo_x() + e.x - _drag['x']}"
                          f"+{root.winfo_y() + e.y - _drag['y']}")
        title.bind("<ButtonPress-1>", _on_drag_start)
        title.bind("<B1-Motion>", _on_drag_motion)

        if os.name == "nt":
            try:
                hwnd = int(root.winfo_id())
                _apply_windows_window_style_hwnd(hwnd, no_activate=True, enable_transparent=False)
            except Exception:
                pass

        def _poll_queue():
            try:
                while not queue.empty():
                    item = queue.get_nowait()
                    if not item:
                        continue
                    kind = item[0]
                    if kind == "log":
                        msg = item[1]
                        text.config(state=tk.NORMAL)
                        text.insert(tk.END, msg + "\n")
                        text.see(tk.END)
                        text.config(state=tk.DISABLED)
                    elif kind == "cmd":
                        cmd, arg = item[1]
                        if cmd == "enable_click_through":
                            if os.name == "nt":
                                try:
                                    hwnd = int(root.winfo_id())
                                    _apply_windows_window_style_hwnd(hwnd, enable_transparent=bool(arg))
                                except Exception:
                                    pass
                        elif cmd == "close":
                            root.quit()
            except Exception:
                pass
            root.after(150, _poll_queue)

        root.after(150, _poll_queue)
        root.mainloop()
    except Exception:
        pass
    finally:
        try:
            root.destroy()
        except Exception:
            pass

def _thread_log_window_server(queue_obj, width=480, height=220, opacity=0.88):
    try:
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        LogWindow._instance.root = root
        try:
            root.attributes("-alpha", opacity)
        except Exception:
            pass

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        x = (screen_w - width) // 2
        y = screen_h - height - 48
        root.geometry(f"{width}x{height}+{x}+{y}")

        bg, fg, title_bg = "#111216", "#e6eef6", "#0f1720"

        title = tk.Frame(root, bg=title_bg, height=28)
        title.pack(fill=tk.X, side=tk.TOP)
        tk.Label(title, text="日志窗口 (thread)", bg=title_bg, fg=fg, padx=8).pack(side=tk.LEFT, padx=(6, 0))

        body = tk.Frame(root, bg=bg)
        body.pack(fill=tk.BOTH, expand=True)
        font = tkfont.Font(family="Consolas", size=11)
        text = tk.Text(body, bg=bg, fg=fg, insertbackground=fg, font=font,
                       wrap=tk.WORD, padx=6, pady=6, bd=0)
        text.config(state=tk.DISABLED)
        vsb = ttk.Scrollbar(body, orient=tk.VERTICAL, command=text.yview)
        text['yscrollcommand'] = vsb.set
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 拖动
        _drag = {"x": 0, "y": 0}
        def _on_drag_start(e):
            _drag["x"], _drag["y"] = e.x, e.y
        def _on_drag_motion(e):
            root.geometry(f"+{root.winfo_x() + e.x - _drag['x']}"
                          f"+{root.winfo_y() + e.y - _drag['y']}")
        title.bind("<ButtonPress-1>", _on_drag_start)
        title.bind("<B1-Motion>", _on_drag_motion)

        def _poll_queue_local():
            try:
                while not queue_obj.empty():
                    item = queue_obj.get_nowait()
                    if not item:
                        continue
                    kind = item[0]
                    if kind == "log":
                        msg = item[1]
                        text.config(state=tk.NORMAL)
                        text.insert(tk.END, msg + "\n")
                        text.see(tk.END)
                        text.config(state=tk.DISABLED)
                    elif kind == "cmd":
                        cmd, arg = item[1]
                        if cmd == "close":
                            root.quit()
            except Exception:
                pass
            root.after(150, _poll_queue_local)

        root.after(150, _poll_queue_local)
        root.mainloop()
    except Exception:
        pass
    finally:
        try:
            root.destroy()
        except Exception:
            pass

class LogWindow:
    _instance = None
    root: Optional[tk.Tk] = None
    _proc: Optional[mp.Process] = None
    _queue: Optional[mp.Queue] = None
    _started = False
    _thread_started = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def start_background(
        self,
        width: int = 480,
        height: int = 220,
        opacity: float = 0.88,
        wait_marker: float = 0.8,
        force_thread: bool = False,
    ) -> None:
        if self.__class__._started:
            return

        marker = os.path.join(os.path.dirname(__file__), "log_window_child_started.txt")
        try:
            os.remove(marker)
        except Exception:
            pass

        if force_thread:
            try:
                q_local = mp.Queue()
                self.__class__._queue = q_local
                th = threading.Thread(target=_thread_log_window_server, args=(q_local, width, height, opacity), daemon=True)
                th.start()
                self.__class__._thread_started = True
                self.__class__._started = True
                log("log_window: started in-thread GUI (force_thread=True)")
                return
            except Exception as e:
                log("log_window: force thread GUI failed:", e)
        try:
            ctx = mp.get_context("spawn")
            q = ctx.Queue()
            p = ctx.Process(target=_log_window_server, args=(q, width, height, opacity), daemon=True)
            p.start()
            self.__class__._proc = p
            self.__class__._queue = q
            t0 = time.time()
            while time.time() - t0 < wait_marker:
                if os.path.exists(marker):
                    self.__class__._started = True
                    return
                time.sleep(0.05)
            if p.is_alive():
                p.terminate()
            print("log_window: child process failed to initialize window -> fallback to thread GUI")
        except Exception as e:
            print("log_window: spawn process failed:", e)

        try:
            q_local = mp.Queue()
            self.__class__._queue = q_local
            th = threading.Thread(target=_thread_log_window_server, args=(q_local, width, height, opacity), daemon=True)
            th.start()
            self.__class__._thread_started = True
            self.__class__._started = True
        except Exception as e:
            print("log_window: fallback thread GUI failed:", e)
            self.__class__._started = False

    def log(self, msg: str):
        try:
            if self.__class__._queue:
                self.__class__._queue.put(("log", str(msg)))
            else:
                print(msg)
        except Exception:
            try:
                print(msg)
            except Exception:
                pass

    def enable_click_through(self, enable: bool = True):
        try:
            if self.__class__._queue:
                self.__class__._queue.put(("cmd", ("enable_click_through", bool(enable))))
        except Exception:
            pass

    def close(self):
        try:
            if self.__class__._queue:
                self.__class__._queue.put(("cmd", ("close", None)))
            if self.__class__._proc:
                self.__class__._proc.join(timeout=0.5)
        except Exception:
            pass

def get_logwin() -> LogWindow:
    return LogWindow()