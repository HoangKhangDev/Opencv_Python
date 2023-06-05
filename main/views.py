from django.http import HttpResponse,StreamingHttpResponse
from django.shortcuts import render
from django.template import loader
# from .index import stream
import cv2
import os
from django.templatetags.static import static
from django.core.files.storage import FileSystemStorage

k=0

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({}, request))

def uploadimage(request):
    print(request.POST.get('upload'))
    print(request.FILES.get('upload'))
    # if request.method == 'POST' and request.FILES['upload']:
    #     myfile = request.FILES['upload']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     print(uploaded_file_url)
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({}, request))


def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render({}, request))

def stream(request):
    template = loader.get_template('stream.html')
    return HttpResponse(template.render({"activeimage":True}, request))



def offwindow(request):
    k=24
    cv2.destroyAllWindows();
    template = loader.get_template('stream.html')
    return HttpResponse(template.render({}, request))



def video(request):
    harcascade = "model/haarcascade_russian_plate_number.xml"

    cap = cv2.VideoCapture(0)

    # cap.set(3, 640)  # width
    # cap.set(4, 480)  # height
    #
    min_area = 500

    while True:
        success, img = cap.read()
        plate_cascade = cv2.CascadeClassifier(harcascade)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
        if k == 27:         # wait for ESC key to exit
            cv2.destroyAllWindows()    
            break    
        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area :
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                img_roi = img[y: y + h, x:x + w]
                cv2.imwrite("main/static/images/save.jpg", img_roi)
                # cv2.destroyAllWindows();
                # template = loader.get_template('stream.html')
                # return HttpResponse(template.render({}, request))
                # cv2.imshow("show rs",img_roi)
        
        template = loader.get_template('stream.html')
        HttpResponse(template.render({}, request))
        cv2.imwrite("result.jpg", img)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('result.jpg', 'rb').read() + b'\r\n')
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("main/static/images" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            cv2.destroyAllWindows();
            count += 1

def video_feed(request):
    return StreamingHttpResponse(video(request), content_type='multipart/x-mixed-replace; boundary=frame')

def close_cv2():
    cv2.destroyAllWindows()

def my_view(request):
    # NOTE: No Content-Length header!
    return StreamingHttpResponse(hello)
    return StreamingHttpResponse(hello(), content_type='multipart/x-mixed-replace; boundary=frame')


def hello():
     yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('main/static/images/save.jpg', 'rb').read() + b'\r\n') 