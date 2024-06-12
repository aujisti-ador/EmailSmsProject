from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        res = super().authenticate(request)
        if res is None:
            return None
        user, token = res
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is not active")
        return user, token
