from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FAQ)


@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["id", "created_at"]
    list_display_links = ["created_at"]


class TourImagesInline(admin.TabularInline):
    model = ImagesTour
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [TourImagesInline]
    list_display = ["id", "title", "created_at"]
    list_filter = ["created_at"]
    list_display_links = ["title"]


admin.site.register(Highlights)
admin.site.register(Overview)
