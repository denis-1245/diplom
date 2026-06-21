from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# Представление для отображения списка опубликованных отзывов и обработки формы
def reviews_view(request):
    review_form = None
    user_has_reviewed = False

    # Логика для АВТОРИЗОВАННЫХ пользователей (проверка и POST)
    if request.user.is_authenticated:
        user_has_reviewed = Review.objects.filter(user=request.user).exists()

        if request.method == 'POST':
            if user_has_reviewed:
                messages.warning(request, "Вы уже оставили отзыв. Спасибо за ваше мнение!")
                return redirect('reviews')

            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.user = request.user
                new_review.is_published = True # Публикуем сразу
                new_review.save()

                messages.success(request, 'Спасибо! Ваш отзыв успешно опубликован.')
                return redirect('reviews')

            else:
                messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')

        if review_form is None:
            review_form = ReviewForm()

    # Получаем список всех опубликованных отзывов
    try:
        published_reviews = Review.objects.filter(is_published=True).order_by('-created_at')
    except Exception:
        published_reviews = []

    context = {
        'reviews': published_reviews,
        'review_form': review_form,
        'user_has_reviewed': user_has_reviewed,
        'user_can_post': request.user.is_authenticated and not user_has_reviewed
    }
    return render(request, 'reviews.html', context)