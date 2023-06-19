from django.contrib import admin
from .models import YoutubePost, Category

admin.site.register(YoutubePost)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)