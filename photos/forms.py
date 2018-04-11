from __future__ import unicode_literals

from django import forms

from .models import Photo


class PhotoForm(forms.Form):
    image = forms.ImageField()
    filtered_image = forms.ImageField()
    content = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea
    )
    created_at = forms.DateTimeField(required=False)
    #
    # class Meta:
    #     model = Photo
    #     fields = ('image', 'content', )
