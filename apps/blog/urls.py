from . import views
from django.urls import path
app_name = 'blog'
urlpatterns = [
    path('', views.show_blog_page, name='blog'),
    path("category/<slug:category_slug>", views.show_blog_by_category, name="category"),
    path("tag/<slug:tag_slug>", views.show_articles_by_tag, name="tag"),
    path('article/<slug:slug>', views.show_article_page, name="article")
]