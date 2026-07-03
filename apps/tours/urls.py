from . import views
from django.urls import path
app_name = "tours"
urlpatterns = [
    path('', views.show_tours_page, name="tours"),
    path('tour-single/<slug:slug>', views.show_tour_page, name="tour-single"),
    path("house-categories/<slug:category_slug>", views.show_house_by_category, name="category")
]
