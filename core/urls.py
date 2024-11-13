from django.urls import path
from core.views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),  # 注册用户的 URL
    path('login/', UserLoginView.as_view(), name='user_login'),  # 登录用户的 URL
]
