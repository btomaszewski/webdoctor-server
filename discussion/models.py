from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class DiscussionThread(models.Model):
    """
    A discussion thread.
    """
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    A comment posted on a discussion thread.
    """
    owner = models.ForeignKey('auth.User')
    discussion = models.ForeignKey(DiscussionThread)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # update the discussion so it's `updated` field will change
        self.discussion.save()
        # now actually call save
        super(Comment, self).save(*args, **kwargs)


class MedicalCase(models.Model):
    """
    A case which is to be discussed. This is attached to a specific
    discussion thread where it should be discussed.
    """
    owner = models.ForeignKey('auth.User')
    discussion = models.ForeignKey(DiscussionThread)
    created = models.DateTimeField(auto_now_add=True)


# This is put here for now because we don't really have a better place
# to put it yet
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create a new token each time the user saves an auth model
    See http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    """
    if created:
        Token.objects.create(user=instance)
