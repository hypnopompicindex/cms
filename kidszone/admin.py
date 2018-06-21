from django.contrib import admin
from .models import Video, Theme
from adminsortable2.admin import SortableAdminMixin


@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image_thumbnail', 'thumbnail', 'active']
    list_editable = ['active',]
    readonly_fields = ('thumbnail', 'image_thumbnail')
    fields = ('title', 'video', 'thumbnail', 'image', 'active')


@admin.register(Theme)
class ThemeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['theme', 'background_image_thumbnail', 'bubble_image_thumbnail']
    readonly_fields = ('background_image_thumbnail', 'bubble_image_thumbnail')
    fields = ('theme', 'background_image', 'bubble_image')

