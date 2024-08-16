import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os
import uuid
import random

def select_zip_file():
    file_path = filedialog.askopenfilename(
        title="选择模组",
        filetypes=[("Minecraft 模组", "*.jar")]
    )
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def process_zip():
    zip_path = entry_path.get()
    if not zip_path.endswith('.zip'):
        messagebox.showerror("错误", "请选择一个 JAR 文件。")
        return

    extract_dir = os.path.splitext(zip_path)[0]

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    random_number = random.randint(1000, 9999)
    new_file_name = f"{random_number}.txt"
    new_file_path = os.path.join(extract_dir, new_file_name)

    with open(new_file_path, 'w') as f:
        f.write(str(uuid.uuid4()))

    new_zip_path = f"{os.path.splitext(zip_path)[0]}_modified.zip"
    with zipfile.ZipFile(new_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, extract_dir))

    for root, dirs, files in os.walk(extract_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(extract_dir)

    messagebox.showinfo("完成", f"已生成新压缩包: {new_zip_path}")

root = tk.Tk()
root.title("模组去特征处理工具")

entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=0, padx=10, pady=10)

btn_browse = tk.Button(root, text="浏览", command=select_zip_file)
btn_browse.grid(row=0, column=1, padx=10, pady=10)

btn_process = tk.Button(root, text="处理压缩包", command=process_zip)
btn_process.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
