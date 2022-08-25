from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class AuthBackend:

    def authenticate(self,email, password):
        try:
            user = User.objects.get(Q(email__iexact=username))
            success = user.check_password(password)
            if success:
                return user

        except User.DoesNotExist:
            pass
        return None

    def get_user(self,uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None