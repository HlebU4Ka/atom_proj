from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
