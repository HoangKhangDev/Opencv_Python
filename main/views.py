from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import cv2
import threading
from django.views.decorators import gzip


@gzip.gzip_page
def index(request):
    try:
        cam=VideoCapture()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except: pass
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())



def detail(request, question_id):
        return HttpResponse("Hello, world. You're at the polls index.")

    # return HttpResponse("You're looking at question %s." % question_id)


def test(request, question_id):
        return HttpResponse("Hello, world. You're at the polls index.")

    # response = "You're looking at the results of question %s."
    # return HttpResponse("response" % question_id)

class VideoCapture(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabber, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
        
    def __del__(self):
        self.video.release()
        
    def getframe(self):
        image=self.frame
        _,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()
    
    def update(self):
        while True:
                    (self.grabber, self.frame) = self.video.read()
                    
def gen(camera):
    while True:
            frame = camera.getframe()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')