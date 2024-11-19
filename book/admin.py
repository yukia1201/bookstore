from django.contrib import admin

# Register your models here.
from book.models import book

# 將資料表註冊到後台管理
class bookAdmin(admin.ModelAdmin):
    list_display = ( 'pubdate', 'publisher', 'bookname', 'author', 'price')
    list_filter = ( 'author', 'publisher')
    search_fields = (['bookname'])
    ordering = (['pubdate'])

# 將資料表註冊到後台管理
admin.site.register(book, bookAdmin)
