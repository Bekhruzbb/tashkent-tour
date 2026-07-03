from . import views
from django.urls import path
app_name = 'main'
urlpatterns = [
    path('', views.show_home_page, name="home"),
    path('about-us/', views.show_about_page, name='about')
]
