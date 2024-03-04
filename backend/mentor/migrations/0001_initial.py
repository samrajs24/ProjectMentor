# Generated by Django 4.2 on 2024-03-04 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('content_type', models.CharField(max_length=50)),
                ('file', models.FileField(blank=True, null=True, upload_to='content/')),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('availability', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SessionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('duration', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='scheduled', max_length=20)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.mentor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]