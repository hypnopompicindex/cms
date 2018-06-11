from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import ContentGroup, ContentCard, ContentLabel, ContentGallery, ContentGroupCard
from adminsortable2.admin import SortableInlineAdminMixin


@admin.register(ContentLabel)
class ContentLabelAdmin(admin.ModelAdmin):
    model = ContentLabel


class ContentGalleryInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ContentGallery


class ContentCardGroupInline(admin.TabularInline):
    model = ContentGroupCard
    extra = 1
    fields = ('content_group', 'label', 'priority')


@admin.register(ContentCard)
class ContentCardAdmin(admin.ModelAdmin):
    model = ContentCard
#    filter_horizontal = ('label',)
    list_display = ('title', 'content_type', 'date_override', 'active', 'parent')
    list_editable = ('active',)
    readonly_fields = ('image_gallery', 'thumbnail', 'parent')
    inlines = [ContentGalleryInline, ContentCardGroupInline]
    fieldsets = (
        ('General', {
            'fields': ('title', 'parent', 'date_override', 'content_type', 'text_position', 'gradient_overlay', 'invert_content_view', 'text_header', 'text', 'video'),
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
    ordering = ('title',)
    inlines = [
        ContentGroupCardInline,
    ]
