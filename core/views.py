from .models import Work
from users.forms import LoginForm, RegistrationForm
from django.shortcuts import render, get_object_or_404
from reviews.models import Review
from django.forms.utils import ErrorList


def home_view(request):
    registration_form_data = request.session.pop('registration_form_data', None)
    registration_form_errors = request.session.pop('registration_form_errors', None)

    if registration_form_data:
        register_form = RegistrationForm(registration_form_data)
        if registration_form_errors:
            register_form._errors = registration_form_errors
    else:
        register_form = RegistrationForm()

    login_form_data = request.session.pop('login_form_data', None)
    login_error_message = request.session.pop('login_error_message', None)

    if login_form_data:
        login_form = LoginForm(request=request, data=login_form_data)

        if login_error_message:
            login_form.non_field_errors().append(login_error_message)
    else:
        login_form = LoginForm()

    try:
        last_works = Work.objects.filter(is_active=True).order_by('-id')[:4]
    except Exception:
        last_works = []

    try:
        last_reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]
    except Exception:
        last_reviews = []

    context = {
        'register_form': register_form,
        'login_form': login_form,
        'last_works': last_works,
        'last_reviews': last_reviews,
    }
    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html', {})


def service_list_view(request):
    return render(request, 'service_list.html', {})


def works_view(request):
    try:
        works_list = Work.objects.filter(is_active=True).order_by('-id')
    except Exception:
        works_list = []

    context = {'works': works_list}
    return render(request, 'works.html', context)


def work_detail_view(request, slug):
    """Отображает детальную страницу конкретной работы, используя slug."""

    # Получаем объект Work по slug или возвращаем 404
    work = get_object_or_404(Work, slug=slug, is_active=True)

    context = {
        'work': work,
    }
    return render(request, 'work_detail.html', context)  # Требуется шаблон work_detail.html


def contacts_view(request):
    return render(request, 'contacts.html', {})