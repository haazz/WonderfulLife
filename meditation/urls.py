from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('category/<str:slug>', views.categories_page),
]