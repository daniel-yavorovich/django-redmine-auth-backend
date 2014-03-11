import redmine
from django.conf import settings
from django.contrib.auth.models import User


class RedmineAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user_info = redmine.Redmine(settings.REDMINE_URL, username=username, password=password).auth()
        except redmine.AuthError:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(
                username=username,
                first_name=user_info.firstname,
                last_name=user_info.lastname,
                email=user_info.mail,
                is_active=True
            )
            user.set_password(password)
            user.save()
        else:
            user.set_password(password)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None