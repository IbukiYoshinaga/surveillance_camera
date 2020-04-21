# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac
from datetime import datetime
import os

# ビデオ設定
video_capture = cv2.VideoCapture(0)

image_count = 0

def start_camera():
  global image_count
  while True:
    #連番の最後の番号から保存する
    dir = 'remote_camera/images'
    directory_name_list       = os.listdir(dir)
    strip_directry_name_list  = []
    if len(directory_name_list) != 0:
      for directory_name_list in directory_name_list:
        strip_directry_name_list.append(int(os.path.splitext(directory_name_list)[0]))
      image_count = max(strip_directry_name_list) + 1

    ret, capture_frame  = video_capture.read()
    save_image_path     = 'remote_camera/images/' + str(image_count) + '.jpg'
    cv2.imwrite(save_image_path, capture_frame)
    image_count += 1

def generate_video():
  global image_count
  while True:
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + open('remote_camera/images/' + str(image_count - 1) + '.jpg' , 'rb').read() + b'\r\n')
