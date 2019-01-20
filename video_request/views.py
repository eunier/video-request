from django.shortcuts import render
from .models import Video


# Create your views here.
def index(request):
    videos = Video.objects.order_by('date_added')
    context = {'videos': videos}
    return render(request, 'video_request/index.html', context)


def vrform(request):
    return render(request, 'video_request/vrform.html')
