from django.contrib import admin
from .models import Content, Mentor, SessionSchedule
# Register your models here.

admin.site.register(Content)
admin.site.register(Mentor)
admin.site.register(SessionSchedule)