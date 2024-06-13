# myapp/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
