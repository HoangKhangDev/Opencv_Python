from django.http import HttpResponse
from django.shortcuts import render

from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
        return HttpResponse("Hello, world. You're at the polls index.")

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
        return HttpResponse("Hello, world. You're at the polls index.")

    # response = "You're looking at the results of question %s."
    # return HttpResponse("response" % question_id)

