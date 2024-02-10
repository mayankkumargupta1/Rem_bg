# forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='',widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'fileUpload',
        'name': 'image',
        'accept': 'image/*',
        'onchange': 'previewImage(event)',
        'label': '',
    }))
