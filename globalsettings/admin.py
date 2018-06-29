from django.contrib import admin, messages
from .models import ContentStyling, VideoWall, Publish
from adminsortable2.admin import SortableAdminMixin
from inline_actions.actions import DefaultActionsMixin, ViewAction
from inline_actions.admin import (InlineActionsMixin,
                                  InlineActionsModelAdminMixin)

@admin.register(ContentStyling)
class ContentStylingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'title_colour',  'text_colour', 'background_colour']
    list_editable = ('title_colour',  'text_colour', 'background_colour')
    fields = ('title_colour', 'text_colour', 'background_colour', 'image')

    def has_add_permission(self, request):
        return False


class PublishActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions = super(PublishActionsMixin, self).get_inline_actions(
            request=request, obj=obj)
        actions.append('publish')
        return actions

    def publish(self, request, obj, parent_obj=None):
        obj.save()
        messages.info(request, ("Published at %s" % obj.publish))

    def get_toggle_publish_label(self, obj):
        return 'Published'

    def get_toggle_publish_css(self, obj):
        return ('button object-tools')


class PublishInline(PublishActionsMixin,
                    InlineActionsMixin,
                    admin.TabularInline):
    model = Publish
    list_display = ('last_published',)
    readonly_fields = ('last_published',)

    def has_add_permission(self, request):
        return False


@admin.register(Publish)
class PublishAdmin(PublishActionsMixin,
                   InlineActionsModelAdminMixin,
                   admin.ModelAdmin):
    list_display = ('publish',)
    readonly_fields = ('publish',)
    exclude = ('videowall',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(VideoWall)
class VideoWallAdmin(admin.ModelAdmin):
    list_display = ['entice_mode_proximity_distance', 'time_out']

    def has_add_permission(self, request):
        return False
