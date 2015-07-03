from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^upload/$',
        views.FileUploadView.as_view(),
        name='upload'),
    url(r'^list/$',
        views.FileListView.as_view(),
        name='list'),
]
