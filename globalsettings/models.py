from django.db import models
from colorfield.fields import ColorField


class ContentCard(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title_colour = ColorField(default='#000000')
    text_colour = ColorField(default='#000000')
    background_colour = ColorField(default='#FFFFF')
    entice_mode_proximity_distance = models.CharField(max_length=255, help_text="centimetres")

    class Meta:
        ordering = ['order']
        verbose_name = 'Content Card'

    def __str__(self):
        return self.title