from django.urls import path
from .views import task_create

urlpatterns = [
    path('create', task_create, name='task_create'),
]