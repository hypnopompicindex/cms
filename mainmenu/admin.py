from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import ContentGroup, ContentCard, ContentLabel, ContentGallery
from adminsortable2.admin import SortableInlineAdminMixin

'''
class ContentCardInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ContentCard
    extra = 1
    fieldsets = (
        ('Content Card', {
            'fields': ('title', 'thumbnail', 'date_override', 'content_type'),
        }),
        ('Image & Image Gallery', {
            'fields': ('image', 'invert_content_view'),
            'classes': ('image_gallery',)
        }),
        ('Text', {
            'fields': ('text',),
            'classes': ('text',)
        }),
        ('Text & Image Gallery', {
            'fields': ('image', 'invert_content_view'),
            'classes': ('text_image_gallery',)
        }),
        ('Video', {
            'fields': ('video',),
            'classes': ('video',)
        }),
        ('Video & Text', {
            'fields': ('video', 'text', 'invert_content_view'),
            'classes': ('video_text',)
        }),
        ('Video with Text Overlay', {
            'fields': ('image', 'text'),
            'classes': ('video_text_overlay',)
        }),
    )
    form = ContentCardForm

    class Media:
        js = ('mainmenu/js/base.js',)
'''

@admin.register(ContentLabel)
class ContentLabelAdmin(admin.ModelAdmin):
    model = ContentLabel


class ContentGalleryInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ContentGallery
#    readonly_fields = ('thumbnail',)
#    fields = ('title', 'image')


@admin.register(ContentCard)
class ContentCardAdmin(admin.ModelAdmin):
    model = ContentCard
    filter_horizontal = ('label',)
    list_display = ('title', 'active', 'priority', 'date_override', 'content_type', 'labels')
    list_editable = ('active', 'priority', 'date_override')
    readonly_fields = ('image_gallery', 'thumbnail')
    inlines = [ContentGalleryInline]

    class Media:
        js = ('mainmenu/js/base.js',)

    def labels(self, obj):
        return ",".join([str(l) for l in obj.label.all()])


@admin.register(ContentGroup)
class ContentGroupAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('item',)
    ordering = ('item',)
#    inlines = [ContentCardInline]
