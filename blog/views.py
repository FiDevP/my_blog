from time import timezone

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from blog.models import Article

from .forms import CommentForm


class ArticleView(ListView):
    """Список статей"""
    article = Article
    queryset = Article.objects.filter(draft=False)
    template_name = 'article/article_list.html'
    paginate_by = 2


class ArticleDetailView(DetailView):

    article = Article
    queryset = Article.objects.all()
    template_name = 'article/article_detail.html'
    slug_field = "url"


class AddComment(View):
    """Отзывы"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        article = Article.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())






