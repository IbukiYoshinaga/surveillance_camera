# -*- coding: utf-8 -*-
import webbrowser
from flask import Flask, Response

from modules.camera_module import get_stream_data

app = Flask(__name__)

stream_data = get_stream_data()

@app.route('/')
def video_stream():
    return Response(stream_data, mimetype='multipart/x-mixed-replace; boundary=boundary')

webbrowser.get().open("http://localhost:8080/")

app.run(host='0.0.0.0', port = 8080, threaded = False)
