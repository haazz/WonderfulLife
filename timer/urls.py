from django.urls import path
from . import views

urlpatterns = [
    path('', views.timer_page),
]