from rest_framework import generics
from .serializers import CircleSerializer, MemberSerializer
from .models import Circle, Member

# Create your views here.


class CircleList(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


class CircleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
