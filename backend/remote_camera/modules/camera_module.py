# -*- coding: utf-8 -*-
import cv2
from uuid import getnode as get_mac

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

def get_stream_data():
  while True:
    ret, capture_frame = video_capture.read()
    camera_recording(False, capture_frame)
    ret, jpg = cv2.imencode("stream_picture.jpg", capture_frame)
    yield b'--boundary\r\nContent-Type: image/jpeg\r\n\r\n' + jpg.tostring() + b'\r\n\r\n'

  video_capture.release()


def camera_recording(release_flag=False, capture_frame=None):
  if(capture_frame is not None):
    video.write(capture_frame)

  if(release_flag == True):
    video.release()
