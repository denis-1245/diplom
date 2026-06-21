from .forms import LoginForm, RegistrationForm

def forms_context(request):
    login_form = LoginForm()
    registration_form = RegistrationForm()

    # --- Логика для формы Входа (LoginForm) ---
    login_form_data = request.session.pop('login_form_data', None)
    login_error_msg = request.session.pop('login_error_message', None)

    if login_form_data:
        login_form = LoginForm(request=request, data=login_form_data)
        login_form.is_valid()

        if login_error_msg:
            login_form.non_field_errors = lambda: [login_error_msg]

    registration_form_data = request.session.pop('registration_form_data', None)

    if registration_form_data:
        registration_form = RegistrationForm(registration_form_data)
        registration_form.is_valid()

    return {
        'login_form': login_form,
        'register_form': registration_form,
    }