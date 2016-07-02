from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Photo

# Create your views here.

class PhotoCreate(CreateView):
    model = Photo
    fields = ('image', 'description', )
    template_name = 'create_photo.html'

    # 유효성 검사 이후에 호출되는 함수.
    def form_valid(self, form):
        new_photo = form.save(commit=False)
        new_photo.user = self.request.user
        new_photo.save()
        return super(PhotoCreate, self).form_valid(form)
