from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api import serializers


# noinspection PyMethodMayBeStatic
class HelloAiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Return a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional view',
            'Gives you the most control over application',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message post request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hellow {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request):
        """Partial Update of the object"""
        return Response({'method': 'PATCH'})

    def delete(self, requests):
        """delete an object"""
        return Response({'method': 'DELETE'})
