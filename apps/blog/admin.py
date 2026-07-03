from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["id", "created_at", "name"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["id", "name", "created_at"]
    list_display_links = ["created_at"]


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["id", "created_at", "title"]
    list_filter = ["created_at"]
    list_display_links = ["title"]


@admin.register(models.PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]

# admin.site.register(models.PhotoGallery)
admin.site.register(models.IPUser)
admin.site.register(models.BlogComment)