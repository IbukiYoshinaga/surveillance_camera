# -*- coding: utf-8 -*-
import cv2
# カスケードファイルの場所
cascade_path = 'face_recognition/cascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# 認識する顔写真
face_image_path = 'face_recognition/images/unknown.jpg'
face_image = cv2.imread(face_image_path)
face_image_gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

#吐き出す画像のpath
output_path = "face_recognition/images/output.jpg"

#minNeighbors,minSizeは物体候補判定
face_rect = cascade.detectMultiScale(
    face_image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))


color = (255, 255, 255)

#unknownが顔として認識された場合
if len(face_rect) > 0:
  for rect in face_rect:
    cv2.rectangle(face_image, tuple(rect[0:2]), tuple(
        rect[0:2]+rect[2:4]), color, thickness=2)
  cv2.imwrite(output_path, face_image)
