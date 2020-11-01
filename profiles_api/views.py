from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api import serializer, models, permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to a traditional django view',
            'Gives you most control over logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello messahe with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Hanlde updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset= [
            'Uses actions (list, create, retrieve etc.)',
            'Autoamtically maps to URLS usng routers',
            'Privides more functioanlity with less code',
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object by its ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle update part of an object by its ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Remove an object by its ID"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,) #trigger has_object_permission function inside permissions.py file
    filter_backends = (filters.SearchFilter,) #always add comma at end to make it to tuple, otherwise error
    search_fields = ('name','email',)


