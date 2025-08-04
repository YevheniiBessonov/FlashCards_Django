from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserLoginForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = "flashCards_auth/login.html"
    redirect_authenticated_user = True
    next_page = "/collections/"


class CustomRegisterView(View):
    template_name = "flashCards_auth/register.html"
    form = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to=self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, f"Account created for {username}")
                return redirect(to=self.success_url)
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
        return render(request, self.template_name, {"form": form})
