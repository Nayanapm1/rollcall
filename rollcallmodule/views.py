from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage, default_storage
from .models import studentrec
import os
from rollcallmodule.Attendance import *

from flask import Flask, request, render_template

# Create your views here.

def r1(request):
    return render(request, 'ComparingPage.html')

def r2(request):
    return render(request, 'coursepopup.html')

def r3(request):
    return render(request, 'ExtractingComparing.html')

def r4(request):
    return render(request, 'History.html')

def r5(request):
    return render(request, 'MyAttendancePage.html')

def r6(request):
    return render(request, 'RollCall.html')

def r7(request):
    return render(request, 'RollCallPage.html')

def r8(request):
    return render(request, 'StudenRecord.html')

def ViewStudentInformation(request):
    return render(request, 'UploadStudentInformationPage.html')

def UploadClassStudentPhoto(request):
    return render(request, 'UploadClassStudentPhotoPage.html')

def upload(request):
    fileitem = request.FILES['filename']
    print(fileitem)
    fs = FileSystemStorage(location='rollcallmodule/StudentUplaodedImages/')
    #fs = default_storage()
    #fs.save(fileitem.name, fileitem)
    fs.save(fileitem.name, fileitem)
    return render(request, 'UploadClassStudentPhotoPage.html')

def Attendancerun(request):
    Run()
    return render(request, 'UploadClassStudentPhotoPage.html')

    # check if the file has been uploaded
    #if fileitem.filename:
        # strip the leading path from the file name
        #fn = os.path.basename(fileitem.filename)
        # open read and write the file into the server
        #open(fn, 'wb').write(fileitem.file.read())

    #app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# def upload(request1):
#     target = os.path.join(APP_ROOT, 'UploadedImages/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#
#     for file in request.files.getlist("file"):
#         print(file)
#         filename = file.filename
#         destination = "/".join([target, filename])
#         print(destination)
#         file.save(destination)
#         print("Upload Complete")
#     return render_template("UploadClassStudentPhotoPage.html")

#def UploadStudentInformation(request):
 #   if request.method== "POST":
 #       studentrec1 = studentrec()
 #       studentrec1.stunum=request.POST.get('stunum')
  #      studentrec1.stuname = request.POST.get('stuname')
  #      studentrec1.selectcourse = request.POST.get('scid')
  #      studentrec1.save()
   #     return HttpResponseRedirect('/rollcallmodule/StudentInformation')

