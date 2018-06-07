from django.db import models
from filebrowser.fields import FileBrowseField


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image_overlay = FileBrowseField("Image Overlay", max_length=200, directory="presentation/image_overlay/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Announcement'

    def __str__(self):
        return self.title