from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from blog.models import Article


class ArticleView(View):
    """Список статей"""
    def get(self, request):
        article = Article.objects.all()
        return render(request, 'article/index.html', {'articles_list': article})


class ArticleDetailView(DetailView):
    """Страница статьи"""
    model = Article
    slug_field = "url"
