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
    video = FileBrowseField("Video", max_length=200, directory="kids_zone/videos/")
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
    bubble_image_1 = FileBrowseField(max_length=200, directory="kids_zone/themes/bubble_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], verbose_name='Bubble Image #1')
    bubble_image_2 = FileBrowseField(max_length=200, directory="kids_zone/themes/bubble_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True, null=True, verbose_name='Bubble Image #2')
    bubble_image_3 = FileBrowseField(max_length=200, directory="kids_zone/themes/bubble_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True, null=True, verbose_name='Bubble Image #3')
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

    def bubble_image_thumbnail_1(self):
        if self.bubble_image_1 and self.bubble_image_1.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="100px" /></a>' % (self.bubble_image_1.url, self.bubble_image_1.url))
        else:
            return ""
    bubble_image_thumbnail_1.short_description = "Bubble Image 1"

    def bubble_image_thumbnail_2(self):
        if self.bubble_image_2 and self.bubble_image_2.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="100px" /></a>' % (self.bubble_image_2.url, self.bubble_image_2.url))
        else:
            return ""
    bubble_image_thumbnail_2.short_description = "Bubble Image 2"

    def bubble_image_thumbnail_3(self):
        if self.bubble_image_3 and self.bubble_image_3.filetype == "Image":
            return mark_safe('<a href="%s" target="_blank"><img src="%s" height="100px" /></a>' % (self.bubble_image_3.url, self.bubble_image_3.url))
        else:
            return ""
    bubble_image_thumbnail_3.short_description = "Bubble Image 3"


@receiver(post_save, sender=Video)
def generate_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/kids_zone/videos/thumbnails/" + str(thumbnail))
