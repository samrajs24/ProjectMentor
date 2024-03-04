from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=50)  # Example: video, audio, PDF, curriculum
    file = models.FileField(upload_to='content/', blank=True, null=True)  # If content type is file-based
    thumbnail_url = models.URLField(blank=True, null=True)  # URL to the thumbnail image

    def __str__(self):
        return self.title

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    availability = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class SessionSchedule(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If users can schedule sessions
    date_time = models.DateTimeField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.mentor.user.username} - {self.date_time}"
