from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/', views.hello, name='hello'),
    path('bye/<str:name>/', views.bye, name='bye'),
]           