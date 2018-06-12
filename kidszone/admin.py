from django.contrib import admin
from .models import Video, Theme
from adminsortable2.admin import SortableAdminMixin


@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image', 'video', 'active']
    list_editable = ('active',)
    readonly_fields = ('thumbnail', 'video_path', 'image_path')
    fields = ('title', 'video', 'thumbnail', 'video_path', 'image', 'image_path', 'active')


@admin.register(Theme)
class ThemeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['theme', 'background_image', 'bubble_image', 'active']
    list_editable = ('active',)
    readonly_fields = ('background_image_path', 'bubble_image_path')
    fields = ('theme', 'background_image', 'background_image_path', 'bubble_image', 'bubble_image_path', 'active')
