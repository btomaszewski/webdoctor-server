from rest_framework import serializers
from discussion.models import DiscussionThread, Comment, MedicalCase


class DiscussionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')

    class Meta:
        model = DiscussionThread
        fields = ('id', 'owner', 'title', 'created', 'updated')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    discussion = serializers.ReadOnlyField(source='discussion.pk')

    class Meta:
        model = Comment
        fields = ('owner', 'discussion', 'content', 'created',)


class MedicalCaseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MedicalCase
        fields = ('owner', 'created', 'discussion',)
