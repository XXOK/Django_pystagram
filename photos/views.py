from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm


# Create your views here.
def hello(request):
    return HttpResponse("안녕하세요 주민 여러분들")


def detail(request, pk, hidden=False):
    if hidden is True:
        # todo: 뭔가 은밀한 작업을 합시다
        pass

    try:
        photo = Photo.objects.get(pk=pk)
        messages = (
            '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
            '<p>주소는 {url}</p>'.format(url=photo.image.url),
        )
        return HttpResponse('\n'.join(messages))
    except:
        photo = get_object_or_404(Photo, pk=pk)
        return photo

def create(request):
    form = PhotoForm()
    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)