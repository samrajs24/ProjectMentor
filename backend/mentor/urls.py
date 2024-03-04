# mentor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs for LearningItem CRUD operations
    path('learning-items/', views.LearningItemsList.as_view(), name='learning-item-list'),
    path('learning-items/<int:pk>/', views.LearningItemDetail.as_view(), name='learning-item-detail'),
    path('learning-items/create/', views.LearningItemCreate.as_view(), name='learning-item-create'),
    path('learning-items/<int:pk>/update/', views.LearningItemUpdate.as_view(), name='learning-item-update'),
    path('learning-items/<int:pk>/delete/', views.LearningItemDelete.as_view(), name='learning-item-delete'),
]
