# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac
from datetime import datetime
import os
import time

# ビデオ設定
video_capture = cv2.VideoCapture(0)

image_count = 0

def start_camera():
  global image_count
  while True:
    #連番の最後の番号から保存する
    dir = 'remote_camera/images'
    in_directory_file_list   = os.listdir(dir)
    strip_directry_file_list = []
    if len(strip_directry_file_list) != 0:
      for directory_file_name in in_directory_file_list:
        if(type(directory_file_name) is int):
          strip_directry_file_list.append(
              int(os.path.splitext(directory_file_name)[0])
          )
      image_count = max(strip_directry_file_list) + 1

    ret, capture_frame = video_capture.read()
    save_image_path    = 'remote_camera/images/' + str(image_count) + '.jpg'
    #cv2.imwrite(save_image_path, capture_frame)
    image_count += 1

def generate_video():
  global image_count
  while True:
    if image_count != 0:
      yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + open('remote_camera/images/' + str(image_count - 1) + '.jpg', 'rb').read() + b'\r\n')

def stream_test():
  while True:
    for num in range(700):
      if num != 0:
        time.sleep(1)
        yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + open('remote_camera/images/' + str(num) + '.jpg', 'rb').read() + b'\r\n')
