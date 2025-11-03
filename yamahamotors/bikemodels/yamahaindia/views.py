from django.shortcuts import render
from . import models
def m(request):
    return render(request,'sample.html')


def s(request):
    return render(request,'service.html')

def v(request):
    return render(request,'r_series.html')

def c(request):
    if request.method=="POST":
        n = request.POST['name']
        e = request.POST['email']
        m = request.POST['message']
        mydata = models.bookorder(un = n, em = e, mss = m)
        mydata.save()
    return render(request,'contact.html')

def mt(request):
    return render(request,'mt_series.html')

def FZ(request):
    return render(request,'FZ_series.html')
