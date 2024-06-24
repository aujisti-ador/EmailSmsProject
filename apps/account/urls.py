from django.urls import path
from .views import RegisterUserView, UpdateUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("update/", UpdateUser.as_view(), name="update_user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]