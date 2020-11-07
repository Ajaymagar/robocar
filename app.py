
from flask import Flask, Response , render_template
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)

face_cascade  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#maskNet = load_model('')
@app.route('/')
def index():
    return render_template('index.html')
'''
def detectAndPredict():
    locs = []
    faces = []
    preds = []
    faces_in_image = face_cascade.detectMultiScale(frame , 1.3 ,5)
    for (x , y , w,h) in faces_in_image:
        locs.append(())
    preds = maskNet.predict(faces)

    return (locs , pred)
'''
def gen(video):
    while True:
        success, image = video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces_in_image = face_cascade.detectMultiScale(gray , 1.3 ,5)
        print(faces_in_image)
        for (x,y,w,h) in faces_in_image:
            cv2.rectangle(image , (x,y),(x+w,y+h),(0,255,0),2)
            break
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
