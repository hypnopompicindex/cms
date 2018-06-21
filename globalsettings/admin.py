from django.contrib import admin
from .models import ContentStyling, VideoWall
from adminsortable2.admin import SortableAdminMixin


@admin.register(ContentStyling)
class ContentStylingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'title_colour',  'text_colour', 'background_colour']
    list_editable = ('title_colour',  'text_colour', 'background_colour')
    fields = ('title_colour', 'text_colour', 'background_colour', 'image')

    def has_add_permission(self, request):
        return False


@admin.register(VideoWall)
class VideoWallAdmin(admin.ModelAdmin):
    list_display = ['entice_mode_proximity_distance', 'time_out']

    def has_add_permission(self, request):
        return False
