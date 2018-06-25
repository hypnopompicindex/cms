from django.db import models
from filebrowser.fields import FileBrowseField
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
import os
from django.utils.safestring import mark_safe
from cms.settings import BASE_DIR
from pathlib import Path


class Sequence(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    active = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    intro_video = FileBrowseField("Intro Video", max_length=200, directory="entice_mode/video_list/intro_video/", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])
    outro_video = FileBrowseField("Outro Video", max_length=200, directory="entice_mode/video_list/outro_video/", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])
    touch_indicator_video = FileBrowseField("Touch Indicator Video", max_length=200, directory="entice_mode/video_list/touch_indicator_video/", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])
    background_vignette_video = FileBrowseField("Background Vignette Video", max_length=200, directory="entice_mode/video_list/background_vignette_video/", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])

    class Meta:
        ordering = ['order']
        verbose_name = 'Video List'

    def __str__(self):
        return self.title

    @property
    def intro_video_thumbnail(self):
        file = Path("media/uploads/entice_mode/video_list/intro_video/thumbnails/%s_thumbnail.png" % self.intro_video.filename_root)
        if file.is_file():
            return mark_safe('<a href="/media/uploads/entice_mode/video_list/intro_video/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/entice_mode/video_list/intro_video/thumbnails/%s_thumbnail.png" height="100px" /></a>' % (self.intro_video.filename_root, self.intro_video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')

    @property
    def outro_video_thumbnail(self):
        file = Path("media/uploads/entice_mode/video_list/outro_video/thumbnails/%s_thumbnail.png" % self.outro_video.filename_root)
        if file.is_file():
            return mark_safe('<a href="/media/uploads/entice_mode/video_list/outro_video/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/entice_mode/video_list/outro_video/thumbnails/%s_thumbnail.png" height="100px" /></a>' % (self.outro_video.filename_root, self.outro_video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')

    @property
    def touch_indicator_video_thumbnail(self):
        file = Path("media/uploads/entice_mode/video_list/touch_indicator_video/thumbnails/%s_thumbnail.png" % self.touch_indicator_video.filename_root)
        if file.is_file():
            return mark_safe('<a href="/media/uploads/entice_mode/video_list/touch_indicator_video/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/entice_mode/video_list/touch_indicator_video/thumbnails/%s_thumbnail.png" height="100px" /></a>' % (self.touch_indicator_video.filename_root, self.touch_indicator_video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')

    @property
    def background_vignette_video_thumbnail(self):
        file = Path("media/uploads/entice_mode/video_list/background_vignette_video/thumbnails/%s_thumbnail.png" % self.background_vignette_video.filename_root)
        if file.is_file():
            return mark_safe('<a href="/media/uploads/entice_mode/video_list/background_vignette_video/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/entice_mode/video_list/background_vignette_video/thumbnails/%s_thumbnail.png" height="100px" /></a>' % (self.background_vignette_video.filename_root, self.background_vignette_video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')


@receiver(post_save, sender=Sequence)
def generate_intro_video_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.intro_video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.intro_video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/entice_mode/video_list/intro_video/thumbnails/" + str(thumbnail))


@receiver(post_save, sender=Sequence)
def generate_outro_video_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.outro_video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.outro_video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/entice_mode/video_list/outro_video/thumbnails/" + str(thumbnail))


@receiver(post_save, sender=Sequence)
def generate_touch_indicator_video_thumbnail(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.touch_indicator_video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.touch_indicator_video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/entice_mode/video_list/touch_indicator_video/thumbnails/" + str(thumbnail))


@receiver(post_save, sender=Sequence)
def generate_background_vignette_video_thumbnail(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.background_vignette_video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.background_vignette_video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/entice_mode/video_list/background_vignette_video/thumbnails/" + str(thumbnail))
