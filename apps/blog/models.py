from django.db import models
from apps.common.models import BaseModel
# Create your models here.


class PhotoGallery(BaseModel):
    image = models.ImageField(upload_to="articels/gallery/images/", verbose_name="Картинки галереи")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


class Category(BaseModel):
    name = models.CharField(max_length=20, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Ссылка категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(BaseModel):
    name = models.CharField(max_length=20, verbose_name='Имя тега')
    slug = models.SlugField(unique=True, verbose_name='Ссылка тега')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Article(BaseModel):
    title = models.CharField(max_length=40, verbose_name='Название статьи')
    photo = models.ImageField(upload_to="article/photos/", verbose_name='Фото поста', null=True)
    date = models.DateField(verbose_name='Дата добавления статьи', auto_now=True)
    text = models.TextField(verbose_name='Текст статьи')
    views = models.ManyToManyField("IPUser", verbose_name="Просмотры API", null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name="Ссылка для поста")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles", verbose_name='категория статей', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="articles", verbose_name="Тег поста", null=True)
    author = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, verbose_name="Автор", null=True)


    def __str__(self):
        return self.title

    def get_first_article(self):
        return self.title.first()

    def count_views(self):
        if self.views:
            return self.views.count()
        else:
            return 0


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class BlogComment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name="статьи комментариев")
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, verbose_name="автор комментария")
    text = models.TextField(null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subcomments",
                               verbose_name="Подкомментарии", null=True, blank=True)

    def __str__(self):
        return f"{self.article.title} - {self.user.username}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class IPUser(models.Model):
    ip_user = models.CharField(max_length=50, verbose_name="IP посетителя")

    def __str(self):
        return self.ip_user

    class Meta:
        verbose_name = "IP"
        verbose_name_plural = "Ips"
