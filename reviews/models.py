from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    car_model = models.CharField(max_length=100, verbose_name="Автомобиль")
    service = models.CharField(max_length=100, verbose_name="Услуга")
    text = models.TextField(verbose_name="Текст отзыва")

    # Варианты выбора оценки
    RATING_CHOICES = (
        (5, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )

    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        # Используем username связанного объекта
        return f'Отзыв от {self.user.username} на {self.car_model}'