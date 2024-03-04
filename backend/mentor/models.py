from django.db import models

class LearningItem(models.Model):
    title = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='mentor_profile_pics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    attachments = models.ManyToManyField('Attachment', blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    book_a_slot = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments')

    def __str__(self):
        return self.name