from django.db import models
from django.utils.text import slugify

class Work(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок/Модель авто")
    description = models.TextField(verbose_name="Описание работы")
    main_media = models.FileField(upload_to='works/main_media/', verbose_name="Главное фото/видео для карточки", blank=True, null=True)
    tags = models.CharField(max_length=255, verbose_name="Теги (через запятую, напр: Керамика, Полировка)")
    duration = models.CharField(max_length=50, verbose_name="Срок выполнения (напр: 3 дня)")
    price = models.CharField(max_length=50, verbose_name="Стоимость (напр: от 35 000 руб.)")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-адрес (Slug)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tags(self):
        # Разбивает строку тегов на список
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        if self.main_media and self.main_media.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return self.main_media.url
        return None

    def get_main_video_url(self):
        if self.main_media and self.main_media.name.lower().endswith(('.mp4', '.mov', '.webm')):
            return self.main_media.url
        return None

class WorkMedia(models.Model):
    """Модель для хранения дополнительных фото и видео для работ."""

    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='media',
        verbose_name="Работа"
    )
    file = models.FileField(upload_to='works/gallery/%Y/%m/%d/', verbose_name="Медиафайл")
    is_image = models.BooleanField(default=True, verbose_name="Это фото?")

    class Meta:
        verbose_name = "Дополнительный медиафайл"
        verbose_name_plural = "Дополнительные медиафайлы"

    def __str__(self):
        return f"{self.work.title} - Медиа №{self.pk}"