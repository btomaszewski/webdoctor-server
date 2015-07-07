from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^auth-token/',
        views.ObtainAuthToken.as_view(),
        name='auth-token'),
    url(r'^test/',
        views.AuthTest.as_view(),
        name='test'),
]

