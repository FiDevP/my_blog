from django.urls import path
from . import views


urlpatterns = [
    path("", views.ArticleView.as_view()),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("comment/<int:pk>/", views.AddComment.as_view(), name="add_comment"),
]
