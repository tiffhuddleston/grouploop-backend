from rest_framework import generics
from .serializers import CircleSerializer, UserSerializer
from .models import Circle, User

# Create your views here.


class CircleList(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


class CircleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
