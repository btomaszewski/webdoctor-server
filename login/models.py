from django.db import models
from django.conf import settings


class PasswordExpiry(models.Model):
    """
    Stores the datetime at which the password will expire.
    This is currently NYI.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='expires')
    date = models.DateTimeField()

