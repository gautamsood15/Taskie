from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('/task/<int:pk>/', TaskList.as_view(), name='tasks'),
]