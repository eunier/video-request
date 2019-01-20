from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'video_request/index.html')


def vrform(request):
    return render(request, 'video_request/vrform.html')
