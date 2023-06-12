from django.db import models


class Entry(models.Model):
    discipline = models.CharField('Предмет', max_length=50)
    time = models.TimeField('Время')

    def __str__(self):
        return self.discipline

    class Meta:
        verbose_name = ' Занятие'
        verbose_name_plural = ' Занятия'
