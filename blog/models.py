from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='слаг', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='img/', **NULLABLE, verbose_name='Изображение')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)
    views = models.DateField(auto_now_add=True, verbose_name='дата')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
