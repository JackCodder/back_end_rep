from django.forms import ValidationError
from rest_framework import serializers
from . import models

class Animal(serializers.ModelSerializer):
    class Meta:
        model = models.Animal
        fields = '__all__'

    def validate(self, attrs):
        if attrs['population'] < 0:
            raise ValidationError('Популяция должна быть положительным числом!')
        
        return attrs