from django import forms
from .models import ContentCard, CONTENT_TYPES

class ContentCardForm(forms.ModelForm):
    class Meta:
        model = ContentCard
        fields = ('content_type',)
        widgets = {
            'date_range': forms.Select(choices=CONTENT_TYPES)
        }