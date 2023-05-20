from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "mysite/index.html")


def a_propos(request):
    return render(request, 'mysite/a-propos.html')


def cv(request):
    return render(request, "mysitee/cv.html")

