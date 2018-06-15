from django.db import models
from filebrowser.fields import FileBrowseField
from django.utils.safestring import mark_safe
from filebrowser.settings import ADMIN_THUMBNAIL


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image_overlay = FileBrowseField("Image Overlay", max_length=200, directory="announcement/image_overlay/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Announcement'

    def __str__(self):
        return self.title

    def image_thumbnail(self):
        if self.image_overlay and self.image_overlay.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" /></a>' % (self.image_overlay.url, self.image_overlay.version_generate(ADMIN_THUMBNAIL).url))
        else:
            return ""
    image_thumbnail.short_description = "Image Overlay"