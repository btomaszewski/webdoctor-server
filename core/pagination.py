from rest_framework import pagination

class CursorPaginatorUpdated(pagination.CursorPagination):
    """
    A cursor paginator using 'updated' as its ordering field
    instead of 'created'
    """
    ordering = '-updated'

class MyCursorPaginator(pagination.CursorPagination):
    """
    Standard cursor paginator using 'created' as its ordering
    field which is specified here even though it is the default.
    """
    ordering = '-created'

class MyPagePaginator(pagination.LimitOffsetPagination):
    """
    Default paginator used by things which can paginate.
    The default page size is 25 but can be increased to 100
    """
    max_limit = 100
