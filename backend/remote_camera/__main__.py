# -*- coding: utf-8 -*-
from modules.camera_module import start_camera
from flask import Flask
import threading
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == "__main__":
    camera_thread = threading.Thread(target=start_camera)

    app = Flask(__name__)
    server_thread = threading.Thread(
      target = app.run
    )

    camera_thread.start()
    server_thread.start()
