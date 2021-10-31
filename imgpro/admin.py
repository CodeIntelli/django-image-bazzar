from django.contrib import admin
from .models import Category, ImageDB
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'description']
    summernote_fields = ('description',)


@admin.register(ImageDB)
class ImageModelAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'description',
                    'image', 'uploaded_date', 'cat']
    summernote_fields = ('description',)
