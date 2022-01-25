from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api import serializers


# noinspection PyMethodMayBeStatic
class HelloAPIViewSets(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)'
            'Automatically maps to URLs',
            'More features , less code'
        ]
        return Response({'message': 'Hello', 'an_apiview': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hellow {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve an particular obj"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Update a field in object"""
        return Response({'method': 'PATCH'})

    def destroy(self, requests, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})


# noinspection PyMethodMayBeStatic
class HelloAPIView(APIView):
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
