# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac
from datetime import datetime

# ビデオ設定
video_capture = cv2.VideoCapture(0)

def start_camera():
  while True:
    ret, capture_frame = video_capture.read()
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = "remote_camera/images/" + date + ".png"
    cv2.imwrite(path, capture_frame)
    print(path)
