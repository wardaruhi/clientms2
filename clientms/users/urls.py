from django.urls import path
from . import views
from .views import SignUpView, ChangePasswordResetDoneSuccessView, ChangePasswordResetDoneView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', ChangePasswordResetDoneView.as_view(), name='password_change'),
    path('password_changedone', ChangePasswordResetDoneSuccessView.as_view(), name = 'password_changedone'),
    path('reset_password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', views.PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_confirmation/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='reset_password_confirmation'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
]
