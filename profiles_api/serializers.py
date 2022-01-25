from rest_framework import serializers


class HelloSerializer(serializers.Serializer):  # noqa
    """Serializes a name field for testing the API"""
    name = serializers.CharField(max_length=20)
