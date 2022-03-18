from email import message
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
from PIL import Image

def daytime_or_night(s, e):
  input_dirpath = s
  output_dirpath = e


  types = ('*.png', '*.gif', '*.JPG')
  img_paths = []
  for t in types:
      img_paths.extend(glob.glob(os.path.join(input_dirpath, t)))


  for path in img_paths:
      img = Image.open(path)
      if img is None:
          print('failed to loading image {}.'.format(path))
          continue

      count = 0
      for i in range(0, 50):
          if (img.getpixel((i, i))[0]) == (img.getpixel((i, i))[1]):
              count += 1
              
      
      if (count == 50):
          img = img.convert('L')

      if img.mode == 'RGB':
          dirpath = os.path.join(output_dirpath, 'Daytime')
      elif img.mode == 'L':
          dirpath = os.path.join(output_dirpath, 'Night')
      else:
          print('image {}: unsupported image type: {}'.format(path, img.mode))
          continue
      os.makedirs(dirpath, exist_ok=True)

      save_path = os.path.join(dirpath, os.path.basename(path))
      img.save(save_path)


    
   