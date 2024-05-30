from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        '''Метод для очищения поля url'''
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL-адрес не соответствует допустимым расширениям изображений.')
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        '''Переопределение метода для получения файла изображения по URL и сохранение файла'''
        image = super().save(commit=False) # создается новый экземпляр изображения
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # скачать изображение с данного URL-адреса
        response = requests.get(image_url) # используется для скачивания изображения путем отправки HTTP-запроса методом GET с использованием URLадреса изображения
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image