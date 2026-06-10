import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import urllib.request
import re
import random
import html
import os

# ----------------- 豪华爆款改写数据库 -----------------

# 1. 闺蜜安利风数据库
BESTIE_HEADERS = [
    "🎀 姐妹们！！今天必须给你们扒一扒这个宝藏！！\n",
    "💖 家人们谁懂啊！亲测好用到哭的宝藏分享，不允许你们不知道！\n",
    "✨ 悄悄告诉你们一个惊天大秘密，这个东西真的绝绝子！\n",
    "🦄 救命！这个神仙单品我真的相见恨晚啊啊啊！\n"
]
BESTIE_EMOJIS = ["🎀", "💖", "✨", "🌸", "😭", "🥺", "🛍️", "💄", "🌈", "🎈", "🧸", "🎉"]
BESTIE_FOOTERS = "\n\n#宝藏女孩 #好物推荐 #小红书爆款 #女生必看 #闺蜜安利 #日常分享 #神仙单品 ✨"

# 2. 深度干货风数据库
DRY_HEADERS = [
    "📌 【硬核预警】全网最全，建议先点赞收藏防迷路！\n",
    "🧠 【深度解析】熬夜整理！把这个底层的逻辑给你盘明白了！\n",
    "📚 【高分干货】用一篇文章，帮你彻底告别迷茫与焦虑！\n",
    "🎯 【保姆级指南】避坑不踩雷！最适合小白的实操手册。\n"
]
DRY_EMOJIS = ["📌", "🎯", "🧠", "📝", "💡", "🔍", "📐", "📈", "⚙️", "🔋", "🔑", "🏆"]
DRY_FOOTERS = "\n\n#提升自己 #干货分享 #学习打卡 #思维模型 #自我成长 #程序员日常 #高能干货 🚀"

# 3. 咆哮震惊风数据库
SHOCK_HEADERS = [
    "🚨 听我一句劝！！千万别再盲目跟风了！！\n",
    "🔥 疯了真的疯了！这简直是降维打击！！\n",
    "⚠️ 避坑警告！不看这篇你绝对会后悔一整年！！\n",
    "💥 震惊！原来这才是最暴力的玩法，全网都在偷偷用！\n"
]
SHOCK_EMOJIS = ["🚨", "🔥", "⚠️", "💥", "😱", "🛑", "💯", "❌", "📣", "🔥", "🧨", "⚡"]
SHOCK_FOOTERS = "\n\n#避坑指南 #震惊幕后 #绝了 #听我一句劝 #爆款打造 #矩阵引流 #不看后悔系列 🚨"


def smart_rewrite(text, style_name):
    """
    三大风格伪原创改写引擎 (带有高端美学排版)
    """
    if not text.strip():
        return ""
    
    # 清洗和分割行
    raw_lines = [line.strip() for line in text.split("\n") if line.strip()]
    cleaned_lines = []
    
    # 基础句子拆分和标点美化
    for line in raw_lines:
        sub_clauses = re.split(r'([。！？])', line)
        for i in range(0, len(sub_clauses)-1, 2):
            clause = sub_clauses[i].strip()
            punc = sub_clauses[i+1]
            if len(clause) > 3:
                cleaned_lines.append(clause + punc)
        # 兜底
        if len(sub_clauses) == 1 and len(sub_clauses[0]) > 3:
            cleaned_lines.append(sub_clauses[0])

    if not cleaned_lines:
        cleaned_lines = raw_lines

    # 1. 闺蜜安利风改写逻辑
    if style_name == "🎀 闺蜜安利风（软萌种草）":
        output = [random.choice(BESTIE_HEADERS), "━━━━━━━━━━━━━━━━━━━\n"]
        for idx, line in enumerate(clean_structure_lines(cleaned_lines)):
            emo1 = random.choice(BESTIE_EMOJIS)
            emo2 = random.choice(BESTIE_EMOJIS)
            if random.random() < 0.3:
                line = line.replace("建议", f"姐妹们闭眼听劝")
                line = line.replace("好", "真的绝绝子")
                line = line.replace("重要", "重要到哭")
            output.append(f"{emo1} {line} {emo2}\n")
        output.append("\n━━━━━━━━━━━━━━━━━━━")
        output.append(BESTIE_FOOTERS)
        
    # 2. 深度干货风改写逻辑
    elif style_name == "📚 深度干货风（专业硬核）":
        output = [random.choice(DRY_HEADERS), "━━━━━━━━━━━━━━━━━━━\n"]
        bullets = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for idx, line in enumerate(clean_structure_lines(cleaned_lines)):
            bullet = bullets[idx % len(bullets)]
            emo = random.choice(DRY_EMOJIS)
            output.append(f"{bullet} 【要点{idx+1}】{line} {emo}\n")
        output.append("\n━━━━━━━━━━━━━━━━━━━")
        output.append(DRY_FOOTERS)
        
    # 3. 咆哮震惊风改写逻辑
    else:
        output = [random.choice(SHOCK_HEADERS), "━━━━━━━━━━━━━━━━━━━\n"]
        for idx, line in enumerate(clean_structure_lines(cleaned_lines)):
            emo1 = random.choice(SHOCK_EMOJIS)
            emo2 = "！！！" if random.random() < 0.5 else ""
            if random.random() < 0.25:
                line = "不听劝的都哭了：" + line
            output.append(f"{emo1} {line}{emo2}\n")
        output.append("\n━━━━━━━━━━━━━━━━━━━")
        output.append(SHOCK_FOOTERS)

    return "\n".join(output)

def clean_structure_lines(lines):
    valid_lines = [l for l in lines if len(l) > 6]
    return valid_lines[:10]


# ----------------- 极客暗黑 GUI 设计 -----------------
class PremiumCopywritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("爆款文案提取与 AI 伪原创助手 v2.0 - 尊享暗黑版")
        self.root.geometry("1000x750")
        self.root.minsize(900, 650)
        
        # 极客暗黑配置
        self.bg_dark = "#121214"       # Obsidian 背景
        self.bg_card = "#1A1A1F"       # 卡片背景
        self.text_main = "#E4E6EB"     # 主白字
        self.text_muted = "#A0A5B1"    # 哑灰字
        self.primary_red = "#FF2E4D"   # 小红书荧光红
        self.accent_green = "#10B981"  # 翡翠绿
        self.accent_blue = "#3B82F6"   # 电光蓝
        
        # Cookie 文件名
        self.cookie_file = "xhs_cookie.txt"
        
        self.root.configure(bg=self.bg_dark)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background=self.bg_dark, foreground=self.text_main, font=("Microsoft YaHei", 10))
        style.configure("TFrame", background=self.bg_dark)
        
        self.setup_ui()
        
    def setup_ui(self):
        # 1. 顶部华丽导航栏
        header_frame = tk.Frame(self.root, bg=self.bg_card, height=75, bd=0)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        brand_bar = tk.Frame(header_frame, bg=self.primary_red, width=6)
        brand_bar.pack(fill=tk.Y, side=tk.LEFT)
        
        title_label = tk.Label(
            header_frame, 
            text="✨ 爆款文案提取与 AI 伪原创助手 ✨", 
            font=("Microsoft YaHei", 16, "bold"), 
            fg=self.primary_red, 
            bg=self.bg_card,
            padx=15
        )
        title_label.pack(side=tk.LEFT)
        
        version_badge = tk.Label(
            header_frame,
            text="PRO v2.0",
            font=("Consolas", 9, "bold"),
            fg="white",
            bg="#333333",
            padx=8,
            pady=2
        )
        version_badge.pack(side=tk.RIGHT, padx=25)

        main_frame = ttk.Frame(self.root, padding=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 3. URL 输入框面板
        url_frame = tk.Frame(main_frame, bg=self.bg_card, padx=15, pady=12, bd=1, relief=tk.FLAT)
        url_frame.pack(fill=tk.X, pady=(0, 15))
        
        url_label = tk.Label(url_frame, text="🔗 网页提取链接 :", font=("Microsoft YaHei", 10, "bold"), fg=self.text_main, bg=self.bg_card)
        url_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.url_entry = tk.Entry(
            url_frame, 
            font=("Microsoft YaHei", 11), 
            bg=self.bg_dark, 
            fg=self.text_main, 
            insertbackground="white",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightcolor=self.primary_red,
            highlightbackground="#2C2C35"
        )
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, padx=5)
        
        # 配置 Cookie 齿轮按钮
        self.cookie_btn = tk.Button(
            url_frame,
            text="⚙️ 配置 Cookie",
            bg="#2D2D35",
            fg=self.text_main,
            font=("Microsoft YaHei", 9, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=12,
            command=self.open_cookie_config
        )
        self.cookie_btn.pack(side=tk.LEFT, padx=(5, 10))
        self.setup_hover_effect(self.cookie_btn, "#2D2D35", "#3F3F4C")
        
        # 提取按钮
        self.extract_btn = tk.Button(
            url_frame, 
            text="一键净化提取", 
            bg=self.primary_red, 
            fg="white", 
            font=("Microsoft YaHei", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#E02443",
            activeforeground="white",
            padx=18,
            command=self.extract_web_text
        )
        self.extract_btn.pack(side=tk.LEFT)
        self.setup_hover_effect(self.extract_btn, self.primary_red, "#E02443")
        
        # 4. 双侧卡片编辑器
        editors_frame = ttk.Frame(main_frame)
        editors_frame.pack(fill=tk.BOTH, expand=True)
        
        # 左卡片
        left_card = tk.Frame(editors_frame, bg=self.bg_card, padx=15, pady=15, bd=1, relief=tk.FLAT)
        left_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        left_title = tk.Label(left_card, text="📝 原文内容 / 粘贴文本区域", font=("Microsoft YaHei", 11, "bold"), fg=self.text_main, bg=self.bg_card)
        left_title.pack(anchor=tk.W, pady=(0, 10))
        
        self.src_text = tk.Text(
            left_card, 
            wrap=tk.WORD, 
            font=("Consolas", 11) if os.name == 'nt' else ("Microsoft YaHei", 10), 
            bg=self.bg_dark, 
            fg=self.text_main,
            insertbackground="white",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#2C2C35",
            highlightcolor=self.accent_blue,
            padx=10,
            pady=10
        )
        self.src_text.pack(fill=tk.BOTH, expand=True)
        
        # 右卡片
        right_card = tk.Frame(editors_frame, bg=self.bg_card, padx=15, pady=15, bd=1, relief=tk.FLAT)
        right_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        right_title_frame = tk.Frame(right_card, bg=self.bg_card)
        right_title_frame.pack(fill=tk.X, pady=(0, 10))
        
        right_title = tk.Label(right_title_frame, text="🚀 爆款 AI 伪原创成品", font=("Microsoft YaHei", 11, "bold"), fg=self.primary_red, bg=self.bg_card)
        right_title.pack(side=tk.LEFT)
        
        style_label = tk.Label(right_title_frame, text="风格人格:", font=("Microsoft YaHei", 9), fg=self.text_muted, bg=self.bg_card)
        style_label.pack(side=tk.RIGHT, padx=(0, 5))
        
        self.style_selector = ttk.Combobox(
            right_title_frame,
            values=["🎀 闺蜜安利风（软萌种草）", "📚 深度干货风（专业硬核）", "🚨 咆哮震惊风（情绪吸睛）"],
            font=("Microsoft YaHei", 9),
            state="readonly",
            width=22
        )
        self.style_selector.pack(side=tk.RIGHT)
        self.style_selector.set("🎀 闺蜜安利风（软萌种草）")
        
        self.dest_text = tk.Text(
            right_card, 
            wrap=tk.WORD, 
            font=("Consolas", 11) if os.name == 'nt' else ("Microsoft YaHei", 10), 
            bg=self.bg_dark, 
            fg=self.text_main,
            insertbackground="white",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#2C2C35",
            highlightcolor=self.primary_red,
            padx=10,
            pady=10
        )
        self.dest_text.pack(fill=tk.BOTH, expand=True)
        
        # 6. 底部科技控制台
        control_frame = tk.Frame(main_frame, bg=self.bg_dark, pady=15)
        control_frame.pack(fill=tk.X)
        
        # 改写按钮
        self.rewrite_btn = tk.Button(
            control_frame, 
            text="⚡ 一键算法改写", 
            bg=self.accent_green, 
            fg="white", 
            font=("Microsoft YaHei", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#059669",
            padx=25,
            pady=6,
            command=self.handle_rewrite
        )
        self.rewrite_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.setup_hover_effect(self.rewrite_btn, self.accent_green, "#059669")
        
        # 复制按钮
        self.copy_btn = tk.Button(
            control_frame, 
            text="📋 复制高赞文案", 
            bg=self.accent_blue, 
            fg="white", 
            font=("Microsoft YaHei", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#2563EB",
            padx=18,
            command=self.copy_to_clipboard
        )
        self.copy_btn.pack(side=tk.LEFT, padx=10)
        self.setup_hover_effect(self.copy_btn, self.accent_blue, "#2563EB")
        
        # 保存按钮
        self.save_btn = tk.Button(
            control_frame, 
            text="💾 导出到文本", 
            bg="#4B5563", 
            fg="white", 
            font=("Microsoft YaHei", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#374151",
            padx=18,
            command=self.save_to_file
        )
        self.save_btn.pack(side=tk.LEFT)
        self.setup_hover_effect(self.save_btn, "#4B5563", "#374151")
        
        # 一键清空
        self.clear_btn = tk.Button(
            control_frame, 
            text="🧹 清空", 
            bg="#2D2D35", 
            fg=self.text_muted, 
            font=("Microsoft YaHei", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#1E1E24",
            padx=18,
            command=self.clear_all
        )
        self.clear_btn.pack(side=tk.RIGHT)
        self.setup_hover_effect(self.clear_btn, "#2D2D35", "#1E1E24")
        
        # 7. 炫酷底层状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("SYSTEM PRO 核心启动成功 | 稳定安全级授权 💚")
        
        status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var, 
            bd=0, 
            anchor=tk.W, 
            font=("Consolas" if os.name == 'nt' else "Microsoft YaHei", 9), 
            bg=self.bg_card, 
            fg=self.text_muted,
            padx=20,
            pady=5
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_hover_effect(self, button, normal_color, hover_color):
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))
        
    def log_status(self, text):
        self.status_var.set(text)
        self.root.update_idletasks()
        
    def clear_all(self):
        self.url_entry.delete(0, tk.END)
        self.src_text.delete("1.0", tk.END)
        self.dest_text.delete("1.0", tk.END)
        self.log_status("CLEAR COMMAND COMPLETED | 已重置就绪")
        
    def open_cookie_config(self):
        """打开华丽的小红书 Cookie 配置子窗口"""
        config_win = tk.Toplevel(self.root)
        config_win.title("⚙️ 配置小红书/防封 Cookie 助手")
        config_win.geometry("520x420")
        config_win.resizable(False, False)
        config_win.configure(bg=self.bg_card)
        config_win.grab_set()  # 模态弹窗
        
        # 标题
        lbl_title = tk.Label(config_win, text="⚙️ 小红书 Cookie 配置中心", font=("Microsoft YaHei", 12, "bold"), fg=self.primary_red, bg=self.bg_card, pady=15)
        lbl_title.pack()
        
        # 图文保姆级指南说明
        guide_text = (
            "💡 简单 3 步，轻松获取小红书防封 Cookie：\n\n"
            "1️⃣ 电脑 Chrome 打开并登录小红书网页版 (xiaohongshu.com)\n"
            "2️⃣ 在网页任意空白处【右键 -> 检查】(或按 F12)，进入开发者工具\n"
            "3️⃣ 依次点击顶部【Application/应用】-> 左侧【Cookies】-> 小红书网址\n"
            "4️⃣ 在右侧列表中找到 [web_session]，双击复制它后面那一长串的值\n"
            "5️⃣ 粘贴在下方框中，点击保存。一次配置，永久不拦截！"
        )
        
        lbl_guide = tk.Label(config_win, text=guide_text, font=("Microsoft YaHei", 9), fg=self.text_main, bg=self.bg_dark, justify=tk.LEFT, padx=15, pady=12, relief=tk.FLAT)
        lbl_guide.pack(fill=tk.X, padx=25, pady=5)
        
        # 输入框
        lbl_input = tk.Label(config_win, text="✏️ 请在此粘贴复制好的 web_session 值 :", font=("Microsoft YaHei", 9, "bold"), fg=self.text_main, bg=self.bg_card, anchor=tk.W)
        lbl_input.pack(fill=tk.X, padx=25, pady=(15, 5))
        
        # 载入现有的 Cookie
        existing_cookie = ""
        if os.path.exists(self.cookie_file):
            try:
                with open(self.cookie_file, "r", encoding="utf-8") as f:
                    existing_cookie = f.read().strip()
            except:
                pass
                
        cookie_entry = tk.Entry(
            config_win,
            font=("Consolas", 10),
            bg=self.bg_dark,
            fg=self.accent_green,
            insertbackground="white",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#2C2C35",
            highlightcolor=self.primary_red
        )
        cookie_entry.pack(fill=tk.X, padx=25, ipady=6, pady=5)
        cookie_entry.insert(0, existing_cookie)
        
        def save_cookie():
            val = cookie_entry.get().strip()
            if not val:
                messagebox.showwarning("保存失败", "Cookie 内容不能为空！", parent=config_win)
                return
            try:
                with open(self.cookie_file, "w", encoding="utf-8") as f:
                    f.write(val)
                self.log_status("COOKIE CONFIG UPDATED | 小红书 Cookie 配置更新成功！")
                messagebox.showinfo("保存成功", "防封 Cookie 已持久化保存！", parent=config_win)
                config_win.destroy()
            except Exception as e:
                messagebox.showerror("IO错误", f"保存失败原因：\n{str(e)}", parent=config_win)
                
        # 保存按钮
        save_btn = tk.Button(
            config_win,
            text="💾 保存配置并应用",
            bg=self.accent_green,
            fg="white",
            font=("Microsoft YaHei", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=5,
            command=save_cookie
        )
        save_btn.pack(pady=20)
        self.setup_hover_effect(save_btn, self.accent_green, "#059669")
        
    def extract_web_text(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("提取错误", "网页链接（URL）不能为空！")
            return
            
        self.log_status("CONNECTING TO HOST... 正在解析远端页面")
        self.root.config(cursor="watch")
        
        # 判断是否是小红书链接
        is_xhs = "xiaohongshu.com" in url
        cookie_val = ""
        
        if is_xhs:
            if os.path.exists(self.cookie_file):
                try:
                    with open(self.cookie_file, "r", encoding="utf-8") as f:
                        cookie_val = f.read().strip()
                except:
                    pass
            # 如果没配置 Cookie，主动弹出配置窗口提示
            if not cookie_val:
                self.root.config(cursor="")
                messagebox.showinfo("Cookie配置提示", "检测到是小红书链接！为了防止小红书官方的风控拦截拦截，请先花 10 秒钟配置一下防封 Cookie 💚")
                self.open_cookie_config()
                return
                
        try:
            req_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            
            # 如果是小红书链接，并且配置了 web_session，则在 HTTP 请求头强行注入 web_session
            if is_xhs and cookie_val:
                req_headers['Cookie'] = f"web_session={cookie_val}"
                self.log_status("SECURITY INJECT | 正在带入安全 Cookie 绕过拦截墙...")
                
            req = urllib.request.Request(url, headers=req_headers)
            
            with urllib.request.urlopen(req, timeout=10) as response:
                html_content = response.read().decode('utf-8', errors='ignore')
                
            # 判断是否被重定向到了拦截墙或登录墙
            if "login" in response.geturl() or "验证码" in html_content or "captcha" in html_content or "<title>登录" in html_content:
                self.root.config(cursor="")
                messagebox.showwarning("拦截警报", "⚠️ 小红书 Cookie 已失效或需要重新滑块解锁！请点击【配置 Cookie】重新更新您的 web_session。")
                self.open_cookie_config()
                return
                
            html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
            html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
            
            raw_text = re.sub(r'<[^>]+>', ' ', html_content)
            decoded_text = html.unescape(raw_text)
            
            lines = [line.strip() for line in decoded_text.splitlines()]
            clean_lines = [line for line in lines if len(line) > 6]
            
            # 去除一些明显的小红书网页无用元数据
            filtered_lines = []
            for l in clean_lines:
                if "小红书" in l and ("登录" in l or "发现" in l or "关于我们" in l):
                    continue
                filtered_lines.append(l)
                
            final_text = "\n".join(filtered_lines[:35])
            
            self.src_text.delete("1.0", tk.END)
            self.src_text.insert(tk.END, final_text)
            
            words_count = len(final_text)
            self.log_status(f"SUCCESS | 成功绕过风控，捕获小红书主体！共 {words_count} 字")
            
        except Exception as e:
            messagebox.showerror("网络错误", f"解析失败，可能需要更新 Cookie，或网络不可达。\n原因：{str(e)}")
            self.log_status("ERROR | 连接受阻，请手动复制文案测试")
        finally:
            self.root.config(cursor="")
            
    def handle_rewrite(self):
        src_content = self.src_text.get("1.0", tk.END).strip()
        if not src_content:
            messagebox.showwarning("数据为空", "未检测到左侧原文，请先粘贴文案！")
            return
            
        selected_style = self.style_selector.get()
        self.log_status(f"RUNNING AI ENGINE... 正在编译[{selected_style}]算法排版中")
        self.dest_text.delete("1.0", tk.END)
        
        # 模拟AI加载
        self.root.after(400, lambda: self._run_rewrite(src_content, selected_style))
        
    def _run_rewrite(self, src_content, style):
        viral_text = smart_rewrite(src_content, style)
        self.dest_text.insert(tk.END, viral_text)
        self.log_status("ALGORITHM TASK COMPLETED | 爆款文案美学排版封装完毕 🎯")
        
    def copy_to_clipboard(self):
        dest_content = self.dest_text.get("1.0", tk.END).strip()
        if not dest_content:
            messagebox.showwarning("拷贝失败", "右侧无改写完成的文案！")
            return
            
        self.root.clipboard_clear()
        self.root.clipboard_append(dest_content)
        self.log_status("CLIPBOARD SYNC SUCCESS | 爆款成品已成功复制到剪贴板 💚")
        messagebox.showinfo("同步成功", "高级排版文案已完美同步到剪贴板，快去发小红书吧！")
        
    def save_to_file(self):
        dest_content = self.dest_text.get("1.0", tk.END).strip()
        if not dest_content:
            messagebox.showwarning("导出失败", "无改写文本可供导出！")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="选择保存位置"
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(dest_content)
            self.log_status(f"EXPORT COMPLETED | 已保存至：{os.path.basename(file_path)}")
            messagebox.showinfo("导出成功", "排版文案已成功导出至本地！")


if __name__ == "__main__":
    root = tk.Tk()
    app = PremiumCopywritingApp(root)
    root.mainloop()