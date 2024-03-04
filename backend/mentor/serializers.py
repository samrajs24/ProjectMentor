# mentor/serializers.py
from rest_framework import serializers
from .models import Mentor, SessionSchedule

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'  

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSchedule
        fields = '__all__'  
