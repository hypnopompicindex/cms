from django.db import models
from filebrowser.fields import FileBrowseField
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
import os
from django.utils.safestring import mark_safe
from cms.settings import BASE_DIR


class Video(models.Model):
    title = models.CharField(max_length=255)
    video = FileBrowseField("Video", max_length=200, directory="kids_zone/videos/", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])
    image = FileBrowseField("Image", max_length=200, directory="kids_zone/images/",
                            extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Video'

    def __str__(self):
        return self.title

    @property
    def thumbnail(self):
        if self.id is None:
            return ''
        else:
            return mark_safe('<img src="/media/uploads/kids_zone/thumbnails/%s_thumbnail.png" width="200" />' % (self.id))


class Theme(models.Model):
    theme = models.CharField(max_length=255)
    background_image = FileBrowseField("Background Image", max_length=200, directory="kids_zone/themes/background_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    bubble_image = FileBrowseField("Bubble Image", max_length=200, directory="kids_zone/themes/bubble_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Theme'

    def __str__(self):
        return self.theme


@receiver(post_save, sender=Video)
def generate_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.id) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/kids_zone/thumbnails/" + str(thumbnail))
