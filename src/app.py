import os
import sys
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import classification


def dirdialog1_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tk.filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)


def dirdialog2_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tk.filedialog.askdirectory(initialdir = iDir)
    entry2.set(iDirPath)


def conductMain():
    text = ""

    SDirPath = entry1.get()
    EDirPath = entry2.get()
    if SDirPath and EDirPath:
        text += "フォルダのパス:" + SDirPath + '\n'
        text += "フォルダのパス:" + EDirPath + '\n'

    if text:
        classification.daytime_or_night(SDirPath, EDirPath)
        tk.messagebox.showinfo("お知らせ", "画像の分類が終わりました")
    else:
        tk.messagebox.showinfo("エラー", "フォルダを指定してください")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("日中と夜の画像分類")

    frame1 = tk.ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    frame2 = tk.ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)
 
    frame3 = tk.ttk.Frame(root, padding=10)
    frame3.grid(row=5, column=1, sticky=W)


    entry1 = tk.StringVar()
    IDirEntry = tk.ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    IDirButton = tk.ttk.Button(frame1, text="入力フォルダの選択", command=dirdialog1_clicked)
    IDirButton.pack(side=LEFT)

    entry2 = tk.StringVar()
    IDirEntry = tk.ttk.Entry(frame2, textvariable=entry2, width=30)
    IDirEntry.pack(side=LEFT)

    IDirButton = tk.ttk.Button(frame2, text="出力フォルダの選択", command=dirdialog2_clicked)
    IDirButton.pack(side=LEFT)


    button1 = tk.ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    button2 = tk.ttk.Button(frame3, text=("閉じる"), command=root.quit)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()
    

    
