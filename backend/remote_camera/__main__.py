# -*- coding: utf-8 -*-
from modules.camera_module import start_camera, generate_video
from flask import Flask, Response
import threading
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    camera_thread = threading.Thread(target=start_camera)

    server_thread = threading.Thread(
        target=app.run
    )

    camera_thread.start()
    server_thread.start()
