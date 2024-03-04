# mentor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs for Mentor CRUD operations
    path('mentors/', views.MentorList.as_view(), name='mentor-list'),
    path('mentors/<int:pk>/', views.MentorDetail.as_view(), name='mentor-detail'),
    path('mentors/create/', views.MentorCreate.as_view(), name='mentor-create'),
    path('mentors/<int:pk>/update/', views.MentorUpdate.as_view(), name='mentor-update'),
    path('mentors/<int:pk>/delete/', views.MentorDelete.as_view(), name='mentor-delete'),

    # URLs for Session CRUD operations
    path('sessions/', views.SessionList.as_view(), name='session-list'),
    path('sessions/<int:pk>/', views.SessionDetail.as_view(), name='session-detail'),
    path('sessions/create/', views.SessionCreate.as_view(), name='session-create'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session-delete'),
]
