from django.shortcuts import render, get_object_or_404
from .forms import PhotoForm
from .models import Photo


def galery(request):
    photos = Photo.objects.all()
    return render(request, 'galery_blog/galery.html', {'photos': photos})
def upload_photo(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'galery_blog/photo_detail.html', {'photo': photo})
