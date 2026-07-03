from django.shortcuts import render, redirect
from .models import ClientReviews, BookingBenefits, RecommendedPackages
from .forms import NewsLetterForm
from apps.tours.models import Tour
from apps.blog.models import Article
from django.http import HttpResponse
# Create your views here.


def show_home_page(request):
    reviews = ClientReviews.objects.all()
    benefits = BookingBenefits.objects.all()
    packages = RecommendedPackages.objects.all()
    tours = Tour.objects.all()
    articles = Article.objects.all()
    first_article = Article.objects.first()
    if request.method == "POST":
        form = NewsLetterForm(data=request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("main:home")
    else:
        form = NewsLetterForm()

    context = {
        'reviews': reviews,
        'benefits': benefits,
        'packages': packages,
        "tours": tours,
        "articles": articles,
        "form": form,
        "first_article": first_article
    }
    return render(request, "main/main.html", context)


def show_about_page(request):
    return render(request, 'main/about.html')