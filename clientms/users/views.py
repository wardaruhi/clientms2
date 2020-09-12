from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

from django.contrib.auth import views as auth_views, forms as auth_forms


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChangePasswordResetDoneView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('password_changedone')

class ChangePasswordResetDoneSuccessView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'password_changedone.html'
