from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Photo, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class PhotoCreate(CreateView):
    model = Photo
    fields = ('title', 'content', 'image', 'description', )
    template_name = 'create_photo.html'

    # 유효성 검사 이후에 호출되는 함수.
    def form_valid(self, form):
        new_photo = form.save(commit=False)
        new_photo.user = self.request.user
        new_photo.save()

        return super(PhotoCreate, self).form_valid(form)

create_photo = login_required(PhotoCreate.as_view())

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == 'POST':
        photo.delete()
        return redirect('photos:list_photo')

    return render(request, 'delete_photo.html', {'photo' : photo})

def view_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    ctx = {
        'photo' : photo,
        'comments' : Comment.objects.filter(photo=photo)
    }

    return render(request, 'detail.html', ctx)

@login_required
def create_comment(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    comment = request.POST.get('comment')

    if request.method == 'POST':
        new_comment = Comment()
        new_comment.photo = photo
        new_comment.content = comment
        new_comment.save()

    return redirect(reverse('photos:view_photo', kwargs={'pk' : photo.pk}))

@login_required
def delete_comment(request, pk):
    if request.method == 'POST':
        comment_pk = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()

    return redirect(reverse('photos:view_photo', kwargs={'pk': pk}))

def list_photo(request):
    per_page = 5
    page = request.GET.get('page', 1)

    photos = Photo.objects.all()

    pg = Paginator(photos, per_page)
    try:
        # Paginator가 page값에 대한 예외처리를 알아서 하지는 않는다. 예외처리는 별도로 한다.
        contents = pg.page(page)
    except PageNotAnInteger:
        contents = pg.page(1)
    except EmptyPage:
        contents = []

    ctx = {
        # template에 전달되는 객체는 page 객체이다. page 객체를 이용해 UI 필요한 여러 편리한 기능을 사용할 수 있다.
        'photos' : contents,
    }

    return render(request, 'list.html', ctx)
