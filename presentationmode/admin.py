from django.contrib import admin
from .models import Presentation
from adminsortable2.admin import SortableAdminMixin


@admin.register(Presentation)
class PresentationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order', 'image_overlay',  'active', 'start_date', 'end_date']
    list_editable = ('active',)