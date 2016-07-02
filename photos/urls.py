
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name='photos'

urlpatterns = [
    # login_required 는 함수를 장식하는 장식자이다. 그런데 Class based View는 클래스이기때문에 장식할 수 없다.
    # 따라서 여기서 as_view()를 할때 한다.
    #url(r'^create/$', login_required(views.PhotoCreate.as_view()), name='create_photo'),
    url(r'^create/$', views.create_photo, name='create_photo'),
    # 참고로 views에서 login_required(views.PhotoCreate.as_view()) 를 변수에 할당해 놓고 그걸 참조하면, urls에서 함수형view인지 클래스형 view인지에 무관하게
    # 똑같은 표현으로 사용할 수 있다.

    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_photo, name='delete_photo'),
    url(r'^view_photo/(?P<pk>[0-9]+)/$', views.view_photo, name='view_photo'),
    url(r'^(?P<pk>[0-9]+)/comment/create/$', views.create_comment, name='create_comment'),
    url(r'^(?P<pk>[0-9]+)/comment/delete/$', views.delete_comment, name='delete_comment'),
    url(r'^list_photo/$', views.list_photo, name='list_photo'),
]