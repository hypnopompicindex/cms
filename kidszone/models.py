from django.db import models
from filebrowser.fields import FileBrowseField
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
import os
from django.utils.safestring import mark_safe
from cms.settings import BASE_DIR
from filebrowser.settings import ADMIN_THUMBNAIL
from pathlib import Path


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

    def thumbnail(self):
        file = Path("media/uploads/kids_zone/videos/thumbnails/%s_thumbnail.png" % self.video.filename_root)
        if file.is_file():
            return mark_safe('<a href="/media/uploads/kids_zone/videos/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/kids_zone/videos/thumbnails/%s_thumbnail.png" height="100px" /></a>' % (self.video.filename_root, self.video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')
    thumbnail.short_description = "Video"

    def image_thumbnail(self):
        if self.image and self.image.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="100px"/></a>' % (self.image.url, self.image.url))
        else:
            return ""
    image_thumbnail.short_description = "Image"


class Theme(models.Model):
    theme = models.CharField(max_length=255)
    background_image = FileBrowseField("Background Image", max_length=200, directory="kids_zone/themes/background_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    bubble_image = FileBrowseField("Bubble Image", max_length=200, directory="kids_zone/themes/bubble_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
#    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Theme'

    def __str__(self):
        return self.theme

    def background_image_thumbnail(self):
        if self.background_image and self.background_image.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="50px" /></a>' % (self.background_image.url, self.background_image.url))
        else:
            return ""
    background_image_thumbnail.short_description = "Background Image"

    def bubble_image_thumbnail(self):
        if self.bubble_image and self.bubble_image.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="100px" /></a>' % (self.bubble_image.url, self.bubble_image.url))
        else:
            return ""
    bubble_image_thumbnail.short_description = "Bubble Image"


@receiver(post_save, sender=Video)
def generate_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/kids_zone/videos/thumbnails/" + str(thumbnail))
