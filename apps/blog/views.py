from django.shortcuts import render, redirect
from .models import *
from .forms import BlogCommentForm
# Create your views here.


def show_blog_page(request):
    articles = Article.objects.all()
    images = PhotoGallery.objects.all()
    context = {
        "articles": articles,
        "images": images
    }
    return render(request, "blog/articles.html", context)


def show_blog_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(category=category)
    context = {
        "category": category,
        "articles": articles
    }
    return render(request, "blog/articles.html", context)


def show_articles_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    articles = Article.objects.filter(tag=tag)
    context = {
        "articles": articles
    }
    return render(request, "blog/articles.html", context)


def get_user_api(request):
    x = request.META.get("HTTP_X_FORWARDED_FOR")
    if x:
        ip = x.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def show_article_page(request, slug):
    articles = Article.objects.all()
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect("blog:article", slug)
    else:
        form = BlogCommentForm()

    ip = get_user_api(request)
    if ip:
        ip_user, created = IPUser.objects.get_or_create(
            ip_user=ip
        )
        article.views.add(ip_user)

    context = {
        "article": article,
        "articles": articles,
        "form": form
    }
    return render(request, "blog/article.html", context)

