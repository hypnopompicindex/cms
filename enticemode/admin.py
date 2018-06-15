from django.contrib import admin
from .models import Sequence
from adminsortable2.admin import SortableAdminMixin


@admin.register(Sequence)
class SequenceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'active']
    list_editable = ('active',)
    readonly_fields = ('intro_video_thumbnail', 'outro_video_thumbnail', 'touch_indicator_video_thumbnail', 'background_vignette_video_thumbnail')
    fieldsets = (
        ('Entice Mode', {
            'fields': ('title', 'start_date', 'end_date', 'active', 'intro_video', 'intro_video_thumbnail', 'outro_video', 'outro_video_thumbnail', 'touch_indicator_video', 'touch_indicator_video_thumbnail', 'background_vignette_video', 'background_vignette_video_thumbnail'),
        }),

    )