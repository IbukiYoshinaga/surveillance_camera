# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac

def get_stream_data():
  # ビデオ設定
  video_capture = cv2.VideoCapture(0)
  video_width   = int(video_capture.get(3))  # カメラの横幅
  video_height  = int(video_capture.get(4))  # カメラの縦幅
  fourcc        = cv2.VideoWriter_fourcc(*'XVID')
  video         = cv2.VideoWriter(
                    'remote_camera/images/video.mp4',
                    fourcc,
                    30,
                    (video_width, video_height)
                  )  # ビデオ設定

  # ビデオ設定
  video_capture = cv2.VideoCapture(0)
  while True:
    ret, capture_frame   = video_capture.read()

    video.write(capture_frame)

    ret, jpg = cv2.imencode("view.jpg", capture_frame)

    yield b'--boundary\r\nContent-Type: image/jpeg\r\n\r\n' + jpg.tostring() + b'\r\n\r\n'

  video_capture.release()
  video.release()
