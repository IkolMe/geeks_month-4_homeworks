from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms


class RegisterView(CreateView):
    # form_class = UserCreationForm
    form_class = forms.CustomUserForm
    template_name = 'users/register.html'
    success_url = '/login/'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LoginView):
    next_page = reverse('users:login')


class UsersListView(ListView):
    model = User
    template_name = 'users/list.html'

    def get_queryset(self):
        return self.model.objects.all()
