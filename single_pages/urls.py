from django.urls import path
from . import views

urlpatterns = {
    path('', views.main_page),
    path('about/', views.about_page),
}