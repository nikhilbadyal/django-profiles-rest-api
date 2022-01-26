from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):  # noqa
    """Serializes a name field for testing the API"""
    name = serializers.CharField(max_length=20)


class UserSerializer(serializers.ModelSerializer):
    """Serialized a user object"""

    class Meta:
        model = models.User
        fields = (
            'id', 'email', 'name', 'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Creates and return a new user"""
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'])
        return user

    def update(self, instance, validated_data):
        """Update a user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
