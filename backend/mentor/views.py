from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Mentor, SessionSchedule
from .serializers import MentorSerializer, SessionSerializer
# Create your views here.

class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

class MentorCreate(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

class MentorUpdate(generics.UpdateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

class MentorDelete(generics.DestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

class SessionList(generics.ListCreateAPIView):
    queryset = SessionSchedule.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SessionSchedule.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

class SessionCreate(generics.CreateAPIView):
    queryset = SessionSchedule.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

class SessionUpdate(generics.UpdateAPIView):
    queryset = SessionSchedule.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

class SessionDelete(generics.DestroyAPIView):
    queryset = SessionSchedule.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
