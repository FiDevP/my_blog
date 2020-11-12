from django.urls import path
from . import views


urlpatterns = [
    path("", views.ArticleView.as_view()),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),

]