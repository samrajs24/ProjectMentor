from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Mentor, SessionSchedule
from .serializers import MentorSerializer, SessionSerializer

from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import Content
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


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        
        # Perform search query against your content model
        results = Content.objects.filter(
            Q(title__icontains=query) |   # Search title field for partial matches
            Q(description__icontains=query)  # Search description field for partial matches
        )
        
        # You may customize this part to format the search results according to your needs
        search_results = []
        for result in results:
            search_results.append({
                'title': result.title,
                'description': result.description,
            })
        
        # Return the search results as JSON response
        return JsonResponse({'results': search_results})
