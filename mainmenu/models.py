from django.db import models
from mptt.models import TreeForeignKey, MPTTModel
from ckeditor.fields import RichTextField
from filebrowser.fields import FileBrowseField
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
import os
from django.utils.safestring import mark_safe
from cms.settings import BASE_DIR


CONTENT_TYPES = (
    ('IMAGE_GALLERY', 'Image Gallery'),
    ('TEXT', 'Text'),
    ('TEXT_GALLERY', 'Text and Image Gallery'),
    ('VIDEO', 'Video'),
    ('VIDEO_TEXT', 'Video and Text'),
    ('VIDEO_TEXT_OVERLAY', 'Video with Text Overlay'),
)


class ContentLabel(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class ContentCard(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
#    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    date_override = models.DateTimeField(blank=True, null=True)
    label = models.ManyToManyField(ContentLabel, blank=True, related_name='labels')
    content_type = models.CharField(max_length=255, choices=CONTENT_TYPES, blank=True, null=True)
    invert_content_view = models.BooleanField(default=False)
    text = RichTextField(blank=True, null=True)
    video = FileBrowseField("Video", max_length=200,
                            directory="main_menu/content_card/videos/",
                            extensions=['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mkv'],
                            blank=True)

    class Meta:
        ordering = ('-priority', 'date_override')

    def __str__(self):
        return self.title

    def image_gallery(selfself):
        return 'To add an Image, click the Gallery link at the top of the page'

    @property
    def thumbnail(self):
        if self.id is None:
            return ''
        else:
            return mark_safe('<img src="/media/uploads/main_menu/content_card/thumbnails/%s_thumbnail.png" width="200" />' % (self.id))


class ContentGallery(models.Model):
    gallery = models.ForeignKey(ContentCard,
                                related_name='galleries',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    title = models.CharField(max_length=255)
    priority = models.PositiveIntegerField(default=0, blank=False, null=False)
    gallery_image = FileBrowseField("Image", max_length=200,
                            directory="main_menu/content_card/images/",
                            extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
                            blank=True)

    class Meta:
        ordering = ['priority']
        verbose_name_plural = 'gallery'

    def __str__(self):
        return self.title


class ContentGroup(MPTTModel):
    item = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=False)
    secret = models.BooleanField(default=False)
    card = models.ManyToManyField(ContentCard, blank=True, related_name='cards')
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'content groups'

    def __str__(self):
        return self.item


@receiver(post_save, sender=ContentCard)
def generate_thumbnails(sender, instance, created, **kwargs):
    if created and instance.video is not None:
        path = BASE_DIR + '/media/' + str(instance.video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.id) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/main_menu/content_card/thumbnails/" + str(thumbnail))
