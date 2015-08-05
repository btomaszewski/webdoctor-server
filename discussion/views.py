from datetime import datetime
from discussion.models import DiscussionThread, Comment, MedicalCase
from discussion.serializers import DiscussionSerializer, CommentSerializer
from discussion.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from core.pagination import MyCursorPaginator


def parse_date_string(ds):
    """
    Parse a datetime object from a string
    :param ds: string which is in the iso6801 format
    :rtype: datetime
    :type ds: string
    """
    format_list = (
        '%Y-%m-%dT%H:%M:%S.%f',
        '%Y-%m-%dT%H:%M:%S.%f',
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%dT%H:%M',
        '%Y-%m-%d',
    )

    # Try each format in succession
    for fmt in format_list:
        try:
            result = datetime.strptime(ds, fmt)
            return result
        except ValueError:
            pass

    # If all the formats failed then raise a value error
    raise ValueError('Cannot parse date')


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View details of a specific comment. Also allows deleting and updating.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class DiscussionList(generics.ListCreateAPIView):
    """
    Returns a list of all discussions. Allows creating new discussions.
    There might need to be a way to pair this down at some point later
    but for now this is good enough.

    Query Parameters:
     * newest - UTC datetime in iso-6801 format which only shows discussions which
                have been updated since this time. This means the time should be
                in the Greenwich Mean Timezone.
    """
    queryset = DiscussionThread.objects.all()
    serializer_class = DiscussionSerializer

    # IsAuthenticated is used so that random people can't just view medical
    # cases without authentication.
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # we override the get method to wrap the list method in an exception
        # handler so we can catch ValueErrors and respond with a specific
        # error instead of the default 500 Internal Server Error
        try:
            return self.list(request, *args, **kwargs)
        except ValueError as e:
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def filter_queryset(self, queryset):
        newest = self.request.query_params.get('newest', None)
        if newest is not None:
            newest_date = parse_date_string(newest).strftime('%Y-%m-%d %H:%M:%S')
            queryset = queryset.filter(updated__gt=newest_date)
        return queryset

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
    pagination_class = MyCursorPaginator
    lookup_field = 'discussion'

    def perform_create(self, serializer):
        # First we get the current discussion using the pk part of the url
        discussion = DiscussionThread.objects.get(pk=int(self.kwargs['pk']))
        # Then we create a new comment using the current user and discussion
        serializer.save(owner=self.request.user, discussion=discussion)
