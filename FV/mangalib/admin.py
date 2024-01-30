from django.contrib import admin
from .models import Author, Book

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
      list_display = ['name']
      list_filter = ['name']
      search_fields = ['name']
      list_per_page = 4


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
      fieldsets = [
             ('Information manga', {'fields': ['title', 'author']}),
             ('Information magasin', {'fields': ['quantity']}),
      ]
      list_display = ['title', 'author', 'quantity']
      list_filter = ['title']
      search_fields = ['title']
      list_per_page = 4


