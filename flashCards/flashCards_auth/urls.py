from django.urls import path
from .forms import CustomPasswordResetForm, CustomSetPasswordForm
from .views import CustomRegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path("login/", CustomLoginView.as_view(template_name="flashCards_auth/login.html"), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("password_reset/", PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        template_name="flashCards_auth/password_reset.html",
        email_template_name="flashCards_auth/emails/reset_password.html",
        subject_template_name="flashCards_auth/emails/reset_password_subject.txt"
    ),
         name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name="flashCards_auth/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        template_name="flashCards_auth/password_reset_confirmation.html",
        form_class=CustomSetPasswordForm
    ), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(
        template_name="flashCards_auth/password_reset_complete.html"
    ), name="password_reset_complete"),
]
