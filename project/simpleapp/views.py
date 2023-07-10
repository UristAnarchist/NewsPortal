from django.views.generic import ListView, DetailView
from .models import News


class NewssList(ListView):
    model = News
    ordering = '-date'
    template_name = 'posts.html'
    context_object_name = 'posts'


class NewsDetail(DetailView):
    model = News
    text = News.text
    template_name = 'post.html'
    context_object_name = 'post'

