from django.db import models
from filebrowser.fields import FileBrowseField
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
import os
from django.utils.safestring import mark_safe
from cms.settings import BASE_DIR


class Videolist(models.Model):
    title = models.CharField(max_length=255)
#    description = models.TextField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    active = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Video List'

    def __str__(self):
        return self.title


class Video(models.Model):
    playlist = models.ForeignKey(Videolist, related_name='videos', on_delete=models.CASCADE)
#    title = models.CharField(max_length=255)
    file = FileBrowseField("Video", max_length=200, directory="wow_mode/playlist/video", extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'])
#    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']

    @property
    def title(self):
        return self.file.filename_root.replace('_', ' ').title()

    @property
    def thumbnail(self):
        if self.id is None:
            return ''
        else:
            return mark_safe('<img src="/media/uploads/wow_mode/playlist/thumbnails/%s_thumbnail.png" width="200" />' % (self.id))


@receiver(post_save, sender=Video, dispatch_uid="create_thumbnail")
def generate_thumbnails(sender, instance, created, **kwargs):
    if created:
        path = BASE_DIR + '/media/' + str(instance.file)
        clip = VideoFileClip(path)
        thumbnail = str(instance.id) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/wow_mode/playlist/thumbnails/" + str(thumbnail))
