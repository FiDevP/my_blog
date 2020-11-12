from time import timezone

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from blog.models import Article


class ArticleView(ListView):
    """Список статей"""
    article = Article
    queryset = Article.objects.filter(draft=False)
    template_name = 'article/article_list.html'


class ArticleDetailView(DetailView):

    article = Article
    queryset = Article.objects.all()
    template_name = 'article/article_detail.html'
    slug_field = "url"




