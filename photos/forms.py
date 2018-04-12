from __future__ import unicode_literals

from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('filtered_image',)
        fields = ('image', 'content', )

    image = forms.ImageField()
    # filtered_image = forms.ImageField()
    content = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'style':'resize:none'}),
    )
    # created_at = forms.DateTimeField(required=False)

    # background - color:  # C5E3D7;