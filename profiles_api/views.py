from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional view',
            'Gives you the most control over application',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
