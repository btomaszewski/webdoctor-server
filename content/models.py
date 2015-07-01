import os.path
from django.db import models
from django.core.exceptions import ValidationError

def name_validator(value):
    """
    Validates that the name field is a valid directory name
    :param value: string to validate
    """
    if os.path.normpath(value) != value:
        raise ValidationError("Invalid name")


class ContentFile(models.Model):
    """
    Represents a content file which will be downloaded by all clients.

    :name: name of the content - same for all versions
    :version: content version
    :file: reference to the actual file in the filesystem
    """
    name = models.CharField(max_length=200, validators=[name_validator,])
    version = models.PositiveIntegerField()
    file = models.FileField(upload_to='./%Y-%m/')

