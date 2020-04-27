from flask import Flask, render_template, Response

from modules.camera_module import VideoCameraClass

app = Flask(__name__)

def generateFrame(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/camera_stream')
def video_feed():
  return Response(generateFrame(VideoCameraClass()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
