from django.urls import path, include
from .views import CustomRegisterView, CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserLoginForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", CustomLoginView.as_view(template_name="flashCards_auth/login.html"), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
