from django.contrib.auth.models import User
from django.db.models import Q


class AuthBackend():
    def authenticate(self,request,username,password):
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
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