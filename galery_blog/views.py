from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import PhotoForm
from .models import Photo


class GaleryListView(ListView):
    model = Photo
    template_name = 'galery_blog/galery.html'
# def galery(request):
#     photo = Photo.objects.all()
#     return render(request, 'galery_blog/galery.html', {'photo': photo})
def upload_photo(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = PhotoForm()
    return render(request, 'galery_blog/upload_photo.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'galery_blog/photo_detail.html', {'photo': photo})
