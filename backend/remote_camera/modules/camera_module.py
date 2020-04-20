# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac
from datetime import datetime
import os

# ビデオ設定
video_capture = cv2.VideoCapture(0)

def start_camera():
  image_count = 0
  while True:
    #連番の最後の番号から保存する
    dir = 'remote_camera/images'
    directory_name_list      = os.listdir(dir)
    strip_directry_name_list = []
    if len(directory_name_list) != 0:
      for directory_name_list in directory_name_list:
        strip_directry_name_list.append(int(os.path.splitext(directory_name_list)[0]))
      image_count = max(strip_directry_name_list) + 1

    ret, capture_frame = video_capture.read()
    date = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = 'remote_camera/images/' + str(image_count) + '.png'
    cv2.imwrite(path, capture_frame)
    image_count += 1
