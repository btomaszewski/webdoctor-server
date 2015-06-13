from django.conf.urls import url
from discussion import views

urlpatterns = [
    url(r'^comments/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(),
        name='comment-detail'),
    url(r'^discussions/$',
        views.DiscussionList.as_view(),
        name='discussion-list'),
    url(r'^discussions/(?P<pk>[0-9]+)/$',
        views.DiscussionDetail.as_view(),
        name='discussion-detail'),
    url(r'^discussions/(?P<pk>[0-9]+)/comments/$',
        views.DiscussionComments.as_view(),
        name='discussion-comments'),
]
