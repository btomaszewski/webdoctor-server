from rest_framework import serializers
from content.models import ContentFile

class ContentFileSerializer(serializers.ModelSerializer):
    version = serializers.ReadOnlyField()
    type = serializers.ReadOnlyField()

    class Meta:
        model = ContentFile
        fields = ('id', 'name', 'version', 'type', 'file')

