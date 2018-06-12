from django.contrib import admin
from .models import Presentation
from adminsortable2.admin import SortableAdminMixin


@admin.register(Presentation)
class PresentationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image_overlay', 'start_date', 'end_date', 'active']
    list_editable = ('active',)
    readonly_fields = ('image_overlay_path',)
    fields = ('title', 'image_overlay', 'image_overlay_path', 'start_date', 'end_date', 'active')