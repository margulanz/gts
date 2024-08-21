from django.contrib import admin

from .models import Tag, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','status']
    prepopulated_fields = {"slug":("title",)}



admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)

