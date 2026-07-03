from django.shortcuts import render
from .models import Tour, HouseType, FAQ, ImagesTour, Highlights, Overview
# Create your views here.


def show_tours_page(request):
    house_types = HouseType.objects.all()
    tours = Tour.objects.all()
    context = {
        "house_types": house_types,
        "tours": tours
    }
    return render(request, "tours/tours.html", context)


def show_house_by_category(request, category_slug):
    house_type = HouseType.objects.get(slug=category_slug)
    tours = Tour.objects.filter(house_type=house_type)
    context = {
        "tours": tours
    }
    return render(request, "tours/tours.html", context)


def show_tour_page(request, slug):
    faqs = FAQ.objects.all()
    tour = Tour.objects.get(slug=slug)
    context = {
        "faqs": faqs,
        "tour": tour
    }
    return render(request, "tours/tour-single.html", context)
