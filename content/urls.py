from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^upload/$',
        views.FileUploadView.as_view(),
        name='upload'),
    url(r'^get/$',
        views.FileListView.as_view(),
        name='list'),
    url(r'^get/(?P<pk>[0-9]+)/$',
        views.FileGetView.as_view(),
        name='get'),
]
