import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def create_zip():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("错误", "请先选择一个文件夹！")
        return

    # 获取保存文件路径
    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", 
                                            filetypes=[("ZIP文件", "*.zip")],
                                            initialfile=os.path.basename(folder))
    if not zip_path:
        return

    # 创建ZIP文件
    try:
        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', folder)
        messagebox.showinfo("成功", "文件夹已成功打包为ZIP文件！")
    except Exception as e:
        messagebox.showerror("错误", f"创建ZIP文件失败: {e}")

# 创建主窗口
root = tk.Tk()
root.title("Minecraft存档打包器")

# 文件夹路径变量
folder_path = tk.StringVar()

# 创建GUI元素
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="选择Minecraft存档文件夹:")
label.pack(anchor="w")

entry = tk.Entry(frame, textvariable=folder_path, width=50)
entry.pack(fill="x")

browse_button = tk.Button(frame, text="浏览...", command=select_folder)
browse_button.pack(pady=5)

zip_button = tk.Button(frame, text="创建ZIP文件", command=create_zip)
zip_button.pack(pady=5)

# 运行主循环
root.mainloop()
