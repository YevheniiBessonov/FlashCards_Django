from django.urls import path
from .views import CustomRegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(template_name="flashCards_auth/login.html"), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
