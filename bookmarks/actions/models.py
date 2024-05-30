from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    '''Модель для хранения действий пользователя'''
    user = models.ForeignKey('auth.User', related_name='actions', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    # поле указывающая на модель ContentType
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    # после  для хранения первичного ключа связанного объекта
    target_id = models.PositiveIntegerField(null=True, blank=True)
    # поле для связанного объекта на основе комбинации двух предыдущих полей
    target = GenericForeignKey('target_ct', 'target_id')


    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct', 'target_id']), # многопольный индекс
        ]
        ordering = ['-created']