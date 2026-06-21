from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
import re


class UsernameOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        try:
            user = CustomUser.objects.get(username__iexact=username)
        except CustomUser.DoesNotExist:
            user = None

        if user is None:
            digits = re.sub(r'[^\d]+', '', str(username))

            if 10 <= len(digits) <= 11:
                normalized_phone = '+7' + digits[-10:]
                try:
                    user = CustomUser.objects.get(phone_number=normalized_phone)
                except CustomUser.DoesNotExist:
                    user = None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None