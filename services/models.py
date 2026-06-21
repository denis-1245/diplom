from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    # Основные поля
    name = models.CharField(
        max_length=200,
        verbose_name='Название услуги/товара'
    )
    category = models.CharField(
        max_length=100,
        verbose_name='Категория',
        default='Общее'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена (руб.)'
    )
    description = models.TextField(
        verbose_name='Краткое описание'
    )

    # Файлы и служебные поля
    image = models.ImageField(
        upload_to='service_images/',
        verbose_name='Фотография',
        null=True,
        blank=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name='URL-идентификатор'
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно для записи/заказа'
    )

    class Meta:
        verbose_name = 'Услуга/Товар'
        verbose_name_plural = 'Услуги и Товары'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)