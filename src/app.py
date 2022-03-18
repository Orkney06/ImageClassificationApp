import os
import sys
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import test


def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tk.filedialog.askdirectory(initialdir = iDir)
    entry.set(iDirPath)


def conductMain():
    text = ""

    dirPath = entry.get()
    if dirPath:
        text += "フォルダのパス:" + dirPath + '\n'

    if text:
        #tk.messagebox.showinfo("info", text)
        test.hello(dirPath)

    else:
        tk.messagebox.showinfo("error", "フォルダを指定してください")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("画像分類")

    frame1 = tk.ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    frame2 = tk.ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)
 
    frame3 = tk.ttk.Frame(root, padding=10)
    frame3.grid(row=5, column=1, sticky=W)


    entry = tk.StringVar()
    IDirEntry = tk.ttk.Entry(frame1, textvariable=entry, width=30)
    IDirEntry.pack(side=LEFT)

    IDirButton = tk.ttk.Button(frame1, text="フォルダの選択", command=dirdialog_clicked)
    IDirButton.pack(side=LEFT)

    button1 = tk.ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    button2 = tk.ttk.Button(frame3, text=("閉じる"), command=quit)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()
    

    
