from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import ContentGroup, ContentCard, ContentLabel, ContentGallery, ContentGroupCard
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


@admin.register(ContentLabel)
class ContentLabelAdmin(admin.ModelAdmin):
    model = ContentLabel


class ContentGalleryInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ContentGallery
    fields = ('priority', 'gallery_image')

    class Media:
        js = ('mainmenu/js/base_gallery.js',)


class ContentCardGroupInline(admin.TabularInline):
    model = ContentGroupCard
    extra = 1
    fields = ('content_group', 'label', 'priority')
    verbose_name = 'Content Group'
    verbose_name_plural = "Content Group"


@admin.register(ContentCard)
class ContentCardAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = ContentCard
#    filter_horizontal = ('label',)
    list_display = ('title', 'content_type', 'parent', 'date_override', 'active')
    list_editable = ('active',)
    readonly_fields = ('image_gallery', 'thumbnail', 'parent', 'video_path')
    inlines = [ContentGalleryInline, ContentCardGroupInline]
    fieldsets = (
        ('General', {
            'fields': ('title', 'button_image', 'parent',  'active', 'date_override', 'content_type', 'text_position', 'text_header', 'gradient_overlay', 'invert_content_view', 'text', 'video', 'thumbnail', 'video_path', 'image_gallery'),
        }),
    )

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
            self.fields = ['title', 'date_override', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'image_gallery', 'thumbnail', 'text_position', 'gradient_overlay']
        else:
            self.fields = ['title', 'date_override', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'image_gallery', 'thumbnail', 'text_position', 'gradient_overlay']
        form = super(ContentCardAdmin,self).get_form(request, obj, **kwargs)
        return form


class ContentGroupCardInline(admin.TabularInline):
    model = ContentGroupCard
    extra = 1
    fields = ('content_card', 'label', 'priority')


@admin.register(ContentGroup)
class ContentGroupAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    readonly_fields = ('subgroups',)
    ordering = ('title',)
    inlines = [
        ContentGroupCardInline,
    ]

    class Media:
        js = ('mainmenu/js/base2.js',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs2 = super().get_queryset(request).filter(secret=False)
        if request.user.is_superuser:
            return qs
        else:
            return qs2

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'button_image', 'parent', 'subgroups', 'secret', 'active']
        else:
            self.fields = ['title', 'button_image', 'parent', 'subgroups', 'active']
        form = super(ContentGroupAdmin, self).get_form(request, obj, **kwargs)
        return form
