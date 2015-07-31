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

def file_validator(value):
    """
    Validates that the filename ends with an accepted extension
    @type value: str
    ":param value: string to validate
    """
    endings = ('.pdf', '.txt', )
    for e in endings:
        if str(value).endswith(e):
            return True
    raise ValidationError('Invalid extension')


class ContentFile(models.Model):
    """
    Represents a content file which will be downloaded by all clients.

    :name: name of the content - same for all versions
    :version: content version
    :file: reference to the actual file in the filesystem
    """

    CONTENT_FILE_TYPES = (
        ('pdf', 'PDF'),
    )

    name = models.CharField(max_length=200, validators=[name_validator, ])
    version = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=CONTENT_FILE_TYPES)
    file = models.FileField(upload_to='./%Y-%m/', validators=[file_validator, ])
