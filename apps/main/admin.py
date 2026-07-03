from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.BookingBenefits)
class BookingBenefitsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'title', 'text']
    list_filter = ['created_at']


@admin.register(models.ClientReviews)
class ClientReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']


@admin.register(models.RecommendedPackages)
class RecommendedPackagesAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "title"]
    list_filter = ["created_at"]
    list_display_links = ["title"]


@admin.register(models.NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    list_filter = ["created_at"]
    list_display_links = ["id"]