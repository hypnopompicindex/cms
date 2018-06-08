from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import ContentGroup, ContentCard, ContentLabel, ContentGallery
from adminsortable2.admin import SortableInlineAdminMixin


@admin.register(ContentLabel)
class ContentLabelAdmin(admin.ModelAdmin):
    model = ContentLabel


class ContentGalleryInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ContentGallery


@admin.register(ContentCard)
class ContentCardAdmin(admin.ModelAdmin):
    model = ContentCard
    filter_horizontal = ('label',)
    list_display = ('title', 'active', 'priority', 'date_override', 'content_type', 'labels')
    list_editable = ('active', 'priority')
    readonly_fields = ('image_gallery', 'thumbnail')
    inlines = [ContentGalleryInline]

    class Media:
        js = ('mainmenu/js/base.js',)

    def labels(self, obj):
        return ",".join([str(l) for l in obj.label.all()])

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs2 = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs2

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'active', 'priority', 'date_override', 'label', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'image_gallery', 'thumbnail', 'text_position', 'gradient_overlay']
        else:
            self.fields = ['title', 'active', 'priority', 'date_override', 'label', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'image_gallery', 'thumbnail', 'text_position', 'gradient_overlay']
        form = super(ContentCardAdmin,self).get_form(request, obj, **kwargs)
        return form


@admin.register(ContentGroup)
class ContentGroupAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    ordering = ('title',)

