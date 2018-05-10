from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from show.models import enter
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from show.serializers import enterSerializer

# Create your views here.

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
 
    # Allow only authenticated users to access this url
    serializer_class = enterSerializer
 
    def get(self, request):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
 
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def enter_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        enter = User.objects.get()
        #user = User.objects.get(email=email, password=password)
        serializer = enterSerializer(enter, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = enterSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
