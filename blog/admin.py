from django.contrib import admin
from .models import Category, Author, Article, Comments


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comments)