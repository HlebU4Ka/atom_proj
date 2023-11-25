from django.urls import path
from .views import CustomUserCreateView, CustomUserLoginView, CustomUserDetailView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-register'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
    path('detail/', CustomUserDetailView.as_view(), name='user-detail'),
]
