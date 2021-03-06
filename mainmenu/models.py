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
from django.utils.html import escape
from django.http import HttpResponse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from pathlib import Path


CONTENT_TYPES = (
    ('IMAGE_GALLERY', 'Image Gallery'),
    ('TEXT', 'Text'),
    ('TEXT_GALLERY', 'Text and Image Gallery'),
    ('VIDEO', 'Video'),
    ('VIDEO_TEXT', 'Video and Text'),
    ('VIDEO_TEXT_OVERLAY', 'Video with Text Overlay'),
    ('IMAGE_TEXT_OVERLAY', 'Image with Text Overlay'),
    ('STOCK CARD', 'Stock Card'),
)

POSITION = (
    ('LEFT', 'Left'),
    ('RIGHT', 'Right'),
)


class ContentLabel(models.Model):
    label = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Content Labels'
        verbose_name_plural = "Content Labels"

    def __str__(self):
        return self.label


class ContentCard(models.Model):
    title = models.CharField(max_length=255)
#    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    date_override = models.DateTimeField(blank=True, null=True)
    label = models.ManyToManyField(ContentLabel, blank=True, related_name='labels')
    content_type = models.CharField(max_length=255, choices=CONTENT_TYPES)
    text_position = models.CharField(max_length=255, choices=POSITION, blank=True, null=True)
    gradient_overlay = FileBrowseField("Gradient overlay", max_length=200, directory="main_menu/content_card/overlay_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True, null=True)
    invert_content_view = models.BooleanField(default=False)
    text_header = models.CharField(max_length=255, blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    video = FileBrowseField("Video", max_length=200,
                            directory="main_menu/content_card/videos/",
                            blank=True, null=True)
#    secret = models.BooleanField(default=False)
    button_image = FileBrowseField(max_length=200, directory="main_menu/content_card/button_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True, null=True, verbose_name='Button Image')
#    image = FileBrowseField(max_length=200, directory="main_menu/content_card/image/", blank=True, null=True, verbose_name='Image')

    class Meta:
        ordering = ('priority', 'creation_date')
        verbose_name = 'Content Card'
        verbose_name_plural = "Content Cards"

    def __str__(self):
        return self.title

    def image_gallery(self):
        return 'To add an Image, click the Gallery link at the top of the page'

    @property
    def thumbnail(self):
        file = Path("media/uploads/main_menu/content_card/videos/thumbnails/%s_thumbnail.png" % self.video.filename_root)
        if file:
            return mark_safe('<a href="/media/uploads/main_menu/content_card/videos/thumbnails/%s_thumbnail.png" target="_blank"><img src="/media/uploads/main_menu/content_card/videos/thumbnails/%s_thumbnail.png" width="200" /></a>' % (self.video.filename_root, self.video.filename_root))
        else:
            return mark_safe('<img src="/media/uploads/no_image_available.png" height="100px" />')

    def parent(self):
        x = '<br> '.join([mark_safe('<a href="/mainmenu/contentgroup/%s/change/">%s</a>' % (p.id, p)) for p in self.contentgroup_set.all()])
        return mark_safe(x)

    @property
    def video_path(self):
        return self.video.path

    @property
    def media(self):
        return str(self.video)

    @property
    def media_timestamp(self):
        return str(self.video.date)

    @property
    def media_button_image(self):
        return str(self.button_image)

    @property
    def media_button_image_timestamp(self):
        return str(self.button_image.date)

    @property
    def media_gradient_overlay(self):
        return str(self.gradient_overlay)

    @property
    def media_gradient_overlay_timestamp(self):
        return str(self.gradient_overlay.date)

    def clean(self):
        super(ContentCard, self).clean()
        msg = "This field is required."

        if self.content_type == 'IMAGE_GALLERY':
            if not self.galleries:
                raise ValidationError("The Gallery field is required.")

        if self.content_type == 'TEXT':
            if not self.text_header:
                raise ValidationError({'text_header': [msg,]})
            if not self.text:
                raise ValidationError({'text': [msg,]})

        if self.content_type == 'TEXT_GALLERY':
            if not self.text_header:
                raise ValidationError({'text_header': [msg,]})
            if not self.text:
                raise ValidationError({'text': [msg,]})
            if not self.text_position:
                raise ValidationError({'text_position': [msg,]})

        if self.content_type == 'VIDEO':
            if not self.video:
                raise ValidationError({'video': [msg,]})

        if self.content_type == 'VIDEO_TEXT':
            if not self.video:
                raise ValidationError({'video': [msg,]})
            if not self.text_header:
                raise ValidationError({'text_header': [msg,]})
            if not self.text:
                raise ValidationError({'text': [msg,]})
            if not self.text_position:
                raise ValidationError({'text_position': [msg,]})

        if self.content_type == 'VIDEO_TEXT_OVERLAY':
            if not self.video:
                raise ValidationError({'video': [msg,]})
            if not self.text_header:
                raise ValidationError({'text_header': [msg,]})
            if not self.text:
                raise ValidationError({'text': [msg,]})
            if not self.text_position:
                raise ValidationError({'text_position': [msg,]})
            if not self.gradient_overlay:
                raise ValidationError({'gradient_overlay': [msg,]})


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
    title = models.CharField(max_length=100, blank=True, null=True)
    card = models.ManyToManyField(ContentCard, blank=True, through='ContentGroupCard')
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)
    secret = models.BooleanField(default=False)
    button_image = FileBrowseField(max_length=200, directory="main_menu/content_group/button_image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True, null=True, verbose_name='Button Image')
    label = models.ManyToManyField(ContentLabel, blank=True, related_name='group_labels')

    class Meta:
        verbose_name = 'Content Groups'
        verbose_name_plural = "Content Groups"

    def __str__(self):
        return self.title

    @property
    def title_for_admin(self):
        if self.parent is None:
            if self.secret is False and self.active is True:
                return mark_safe('<span style="color:black;">%s</span>' % (self.title))
            if self.secret is False and self.active is False:
                return mark_safe('<span style="color:#a1a1a1;">%s</span>' % (self.title))
            if self.secret is True and self.active is True:
                return mark_safe('<span style="color:#1445e5;">%s</span>' % (self.title))
            if self.secret is True and self.active is False:
                return mark_safe('<span style="color: #9baeea;">%s</span>' % (self.title))
        else:
            return '%s' % (self.title)

    @property
    def subgroups(self):
        x = '<br> '.join([mark_safe('<a href="/mainmenu/contentgroup/%s/change/">%s</a>' % (p.id, p)) for p in self.children.all()])
#        return x
#        x = '<br> '.join(([str(p) for p in self.children.all()]))
#        y = ([str(p.id) for p in self.children.all()])
        return mark_safe(x)

    @property
    def media(self):
        return str(self.button_image)

    @property
    def media_timestamp(self):
        return str(self.button_image.date)


class ContentGroupCard(models.Model):
    title = models.CharField(max_length=255)
    content_card = models.ForeignKey(ContentCard, on_delete=models.CASCADE)
    content_group = models.ForeignKey(ContentGroup, blank=True, on_delete=models.CASCADE)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    label = models.ManyToManyField(ContentLabel, blank=True, related_name='group_card_labels')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('creation_date',)
        verbose_name = 'Content Card'
        verbose_name_plural = "Content Cards"
        unique_together = ('content_card', 'content_group')

    def __str__(self):
        return self.title


@receiver(post_save, sender=ContentCard)
def generate_thumbnails(sender, instance, created, **kwargs):
    try:
        path = BASE_DIR + '/media/' + str(instance.video)
        clip = VideoFileClip(path)
        thumbnail = str(instance.video.filename_root) + '_thumbnail.png'
        clip.save_frame(thumbnail, t=(clip.duration/2))
        os.rename(BASE_DIR + '/' + str(thumbnail), BASE_DIR + "/media/uploads/main_menu/content_card/videos/thumbnails/" + str(thumbnail))
    except OSError:
        pass
