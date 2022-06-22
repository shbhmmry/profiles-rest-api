from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    def post(self,request):
        """crate a hello message with your name"""   
        serializer = self.serializers_class(data=request.data)
        """The self.serializer_class function is a function that comes with the APIview that 
        retrieves the configured serializer class for our view so it's the
        standard way that you should retrieve the serializer class when working with
        serializers in a view
        """
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            """
            we're going to be validating that the name is no longer than 10 characters the
            way you validate a serializer is you call  is_valid class so you can type
            if serializer.is_valid
            """


            message = f'Hello {name}'  #F string functionality inserts a variable into a string
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )        
            """
            this was an error we need to change this to a 400 bad
            request so we return the standard error response code for this type of error in an API 
            Now you could pass in just an integer 400 here however it's good to use this
            status object here to get it because
            then you can easily see what the request means when you're looking at the code so
            we know this 400 bad request means there was a bad request made to our API
            """                
    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})  