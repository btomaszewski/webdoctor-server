from rest_framework import serializers

class NewUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new AuthUser instance.
        """
        pass

    def update(self, instance, validated_data):
        """
        Update and return an existing AuthUser instance given the validated data
        """
        pass

