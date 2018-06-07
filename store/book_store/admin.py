from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publish', 'status',)
    list_filter = ('status', 'publish_date', 'publish', 'publisher')
    search_fields = ('title', 'isbn')
    raw_id_fields = ('publisher',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Book, BookAdmin)
