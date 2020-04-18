# -*- coding: utf-8 -*-
import cv2

# カスケードファイルの場所
cascade_path = 'face_recognition/cascades/haarcascade_frontalface_default.xml'
cascade      = cv2.CascadeClassifier(cascade_path)

#吐き出す画像のpath
output_face_path   = "face_recognition/images/output_face.jpg"
output_around_path = "face_recognition/images/output_around.jpg"

video_capture = cv2.VideoCapture(0)
video_width   = int(video_capture.get(3))  # カメラの横幅
video_height  = int(video_capture.get(4))  # カメラの縦幅
fourcc        = cv2.VideoWriter_fourcc(*'XVID')
video         = cv2.VideoWriter(
                  'face_recognition/images/video.mp4',
                  fourcc,
                  30,
                  (video_width, video_height)
                )  # ビデオ設定

while(True):
  ret, capture_frame   = video_capture.read()
  #カメラが重すぎるためリサイズ
  resize_capture_frame = cv2.resize(capture_frame, (0, 0), fx=0.5, fy=0.5)
  face_image_gray      = cv2.cvtColor(resize_capture_frame, cv2.COLOR_BGR2GRAY)
  #minNeighbors,minSizeは物体候補判定
  face_rect = cascade.detectMultiScale(
                face_image_gray,
                scaleFactor=1.1,
                minNeighbors=2,
                minSize=(30, 30)
              )

  outline_color = (255, 255, 255)

  #unknownが顔として認識された場合
  if len(face_rect) > 0:
    for rect in face_rect:
      cv2.rectangle(resize_capture_frame, tuple(rect[0:2]), tuple(
        rect[0:2]+rect[2:4]), outline_color, thickness=2)
    cv2.imwrite(output_face_path, resize_capture_frame)

  video.write(capture_frame)

  cv2.imshow('frame', resize_capture_frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
video.release()
cv2.destroyAllWindows()
