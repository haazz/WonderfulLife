from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, YoutubePost

# Create your views here.
class PostList(ListView):
    model = YoutubePost
    template_name = 'meditation/post_list.html'
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = YoutubePost.objects.filter(category=None).count()

        return context

def categories_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = YoutubePost.objects.filter(category=category)

    context = {
        'category': category,
        'categories': Category.objects.all(),
        'no_category_count': YoutubePost.objects.filter(category=None).count(),
        'youtubepost_list': post_list,
    }
    return render(request, 'meditation/post_list.html', context)