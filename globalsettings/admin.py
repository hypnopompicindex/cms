from django.contrib import admin
from .models import ContentCard
from adminsortable2.admin import SortableAdminMixin


@admin.register(ContentCard)
class ContentCardAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order', 'title_colour',  'text_colour', 'background_colour']
    list_editable = ('title_colour',  'text_colour', 'background_colour')