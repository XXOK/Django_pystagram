from django.contrib import admin
from photos.models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'filtered_image', 'content', 'created_at']

admin.site.register(Photo, PhotoAdmin)