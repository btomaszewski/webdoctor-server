from discussion.models import DiscussionThread, Comment, MedicalCase
from discussion.serializers import DiscussionSerializer, CommentSerializer
from discussion.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class DiscussionList(generics.ListCreateAPIView):
    """
    Returns a list of all discussions. Allows creating new discussions.
    There might need to be a way to pair this down at some point later
    but for now this is good enough.
    """
    queryset = DiscussionThread.objects.all()
    serializer_class = DiscussionSerializer

    # IsAuthenticated is used so that random people can't just view medical
    # cases without authentication.
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DiscussionDetail(generics.RetrieveUpdateAPIView):
    """
    Display details about the discussion and allow updating it's data.
    """
    queryset = DiscussionThread.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class DiscussionComments(generics.ListCreateAPIView):
    """
    This view is a view of a given discussion and allows creating a new
    comment in the context of that discussion.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'discussion'

    def perform_create(self, serializer):
        # First we get the current discussion using the pk part of the url
        discussion = DiscussionThread.objects.get(pk=int(self.kwargs['pk']))
        # Then we create a new comment using the current user and discussion
        serializer.save(owner=self.request.user, discussion=discussion)
