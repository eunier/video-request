from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm


# Create your views here.
def index(request):
    videos = Video.objects.order_by('date_added')
    context = {'videos': videos}
    return render(request, 'video_request/index.html', context)


def vrform(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            new_req = Video(
                video_title=request.POST['video_name'],
                video_desc=request.POST['video_desc']
            )
            new_req.save()
            # redirect to home page (index)
            return redirect('index')
    else:
        form = VideoForm()

    context = {'form': form}

    return render(request, 'video_request/vrform.html', context)
