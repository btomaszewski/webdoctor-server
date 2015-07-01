from django.db.models import Q, Max
from django.http import Http404
from rest_framework import generics, views, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from content.models import ContentFile
from content.serializers import ContentFileSerializer

def str_to_bool(s):
    return s.lower() == 'true'

class FileUploadView(generics.CreateAPIView):
    """
    The FileUploadView. Please note that we don't use JSON here. For this view
    we use the multipart parser. Clients should be careful of this. Also note
    that although names are supposed to be case-insensitive try to use the same
    case for the names.
    """
    permission_classes = (permissions.IsAdminUser,)
    parser_classes = (FormParser, MultiPartParser,)
    serializer_class = ContentFileSerializer

    def perform_create(self, serializer):
        current_count = len(ContentFile.objects.filter(name__iexact=self.request.data['name']))
        serializer.save(version=current_count + 1)


class FileListView(generics.ListAPIView):
    """
    To only see the latest versions of each category add latest=true as a query
    parameter. Using name=<category> will filter the results by name. Using
    version=<version> will show only files of that version. name and version
    can be combined but latest is exclusive so if you specify latest=true
    then name and version will be ignored.
    """

    serializer_class = ContentFileSerializer

    def get_queryset(self):
        queryset = ContentFile.objects.all()
        name = self.request.query_params.get('name', None)
        version = self.request.query_params.get('version', None)
        latest = str_to_bool(self.request.query_params.get('latest', 'false'))
        if latest:
            filter_list = ContentFile.objects.values('name').annotate(version=Max('version'))
            # Exclude everything we don't want. It's not great but it will
            # have to do for now.
            for i in filter_list:
                queryset = queryset.exclude(~Q(version=i['version']), name__iexact=i['name'])
        else:
            if name is not None:
                queryset = queryset.filter(name__iexact=name)
            if version is not None:
                queryset = queryset.filter(version=version)
        return queryset


class FileGetView(views.APIView):

    def get(self, request, pk):
        try:
            file = ContentFile.objects.get(pk=pk)
            print(file.file)
        except ContentFile.DoesNotExist:
            raise Http404()
