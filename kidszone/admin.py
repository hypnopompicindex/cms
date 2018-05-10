from django.contrib import admin
from .models import Video, Theme
from adminsortable2.admin import SortableAdminMixin


@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'video', 'active']
    list_editable = ('active',)
    readonly_fields = ('thumbnail',)


@admin.register(Theme)
class ThemeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['theme', 'background_image', 'bubble_image', 'active']
    list_editable = ('active',)