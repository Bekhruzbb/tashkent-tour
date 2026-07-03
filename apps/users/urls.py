from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path("login/", views.show_login_page, name="login"),
    path("registration", views.show_registration_page, name="registration"),
    path('auth/', views.login_user, name='auth'),
    path('register-user/', views.register_user, name='register'),
    path("exit/", views.logout_user, name="logout")
]
