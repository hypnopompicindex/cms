from django.db import models
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from filebrowser.fields import FileBrowseField


class ContentStyling(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title_colour = ColorField(default='#000000')
    text_colour = ColorField(default='#000000')
    background_colour = ColorField(default='#FFFFF')
    image = FileBrowseField("Image", max_length=200, directory="global_settings/image/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], blank=True)

    class Meta:
        ordering = ['order',]
        verbose_name = 'Content Styling'
        verbose_name_plural = "Content Styling"

    def __str__(self):
        return self.title


class VideoWall(models.Model):
    entice_mode_proximity_distance = models.IntegerField(help_text="millimetres", validators=[MinValueValidator(0), MaxValueValidator(300)])
