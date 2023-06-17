from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, YoutubePost

# Create your views here.
class PostList(ListView):
    model = YoutubePost
    ordering = '-pk'


    image_link = link.replace('www', 'img') + "/2.jpg"
