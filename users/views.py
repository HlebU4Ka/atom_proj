from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from settings_app.serializers import SignupSerializer


class CustomUserCreateView(CreateView):
    model = get_user_model()
    template_name = 'registration/register.html'
    fields = ['email', 'name', 'password']
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'registration/user_detail.html'
    context_object_name = 'user'


class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({"access_token": access_token, "refresh_token": refresh_token},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
