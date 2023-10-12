from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='img/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    changes_date = models.DateField(auto_now_add=True, verbose_name='дата изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=150, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак версии')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.version_number} {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
