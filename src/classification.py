import os
import sys
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import app
import cv2
import glob
import numpy as np

def hello(s):
  types = ('*.png', '*.gif', '*.jpg')
  img_paths = []
  for t in types:
      img_paths.extend(glob.glob(os.path.join(s, t)))
  str(img_paths)
  img = cv2.imread(str(img_paths))
  tk.messagebox.showinfo("info", img_paths)