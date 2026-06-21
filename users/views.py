import re
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            request.session['registration_form_data'] = request.POST
            request.session['registration_form_errors'] = form.errors
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме регистрации.')
            return redirect('/#registerModal')
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        login_data = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me')  # Получаем значение галочки

        user = authenticate(request, username=login_data, password=password)

        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)

            messages.success(request, f'С возвращением, {user.username}!')
            return redirect('profile')
        else:
            request.session['login_error_message'] = 'Неверный логин/телефон или пароль.'
            return redirect('/#loginModal')
    return redirect('home')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Вы вышли из системы.")
    return redirect('home')

@login_required
def profile_view(request):
    """Отображает страницу профиля текущего авторизованного пользователя."""
    context = {
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)