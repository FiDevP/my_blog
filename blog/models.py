from django.db import models
from datetime import datetime

from django.urls import reverse


class Category(models.Model):
    """Категории"""

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    """Авторы"""

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Почта", max_length=100)
    avatar = models.ImageField("Аватар", upload_to="autors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    """Статьи"""

    name = models.CharField("Название", max_length=150)
    image = models.ImageField("Обложка", upload_to="articles/")
    text = models.TextField("Текст")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    category = models.ManyToManyField(Category, verbose_name="Категория")
    draft = models.BooleanField("Черновик", default=False)
    datetime = models.DateTimeField("Время", default=datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"slug": self.url})

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comments(models.Model):
    """Комментарии"""

    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст")
    datetime = models.DateTimeField("Время", default=datetime.now)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"