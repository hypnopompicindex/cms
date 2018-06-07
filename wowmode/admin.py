from django.contrib import admin
from .models import Videolist, Video
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class VideoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Video
    readonly_fields = ('thumbnail',)
    fields = ('order', 'title', 'thumbnail', 'file')


@admin.register(Videolist)
class VideolistAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date',  'active']
    list_editable = ('active',)
    inlines = [VideoInline]