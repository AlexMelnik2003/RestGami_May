from django.urls import path
from .views import TaskAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

urlpatterns = [
    path('api/list', TaskAPIView.as_view()),
    path('api/create', CreateAPIView.as_view()),
    path('api/update', UpdateAPIView.as_view()),
    path('api/delete', DestroyAPIView.as_view()),
]
