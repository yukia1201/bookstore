from django.contrib import admin

# Register your models here.
from book.models import book

# 將資料表註冊到後台管理
admin.site.register(book)