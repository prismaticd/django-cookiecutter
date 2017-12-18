import logging

from allauth.account import views as allauth_views
from django.core.urlresolvers import reverse_lazy

logger = logging.getLogger(__name__)


class MySignupView(allauth_views.SignupView):
    template_name = "register.html"
    success_url = reverse_lazy('profile:edit')


class MyLoginView(allauth_views.LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('profile:edit')


class MyEmailView(allauth_views.EmailView):
    template_name = "email.html"
    #success_url = reverse_lazy('profile:edit')


class MyConfirmEmailView(allauth_views.ConfirmEmailView):
    success_url = reverse_lazy('profile:edit')


class MyPasswordChangeView(allauth_views.PasswordChangeView):
    template_name = "password_change.html"
    success_url = reverse_lazy('profile:edit')


class MyPasswordSetView(allauth_views.PasswordSetView):
    template_name = "password_set.html"
    success_url = reverse_lazy('home_app:home-page')


class MyPasswordResetView(allauth_views.PasswordResetView):
    template_name = "password_reset.html"
    # success_url = reverse_lazy('account_login')


class MyPasswordResetDoneView(allauth_views.PasswordResetDoneView):
    template_name = "password_reset_done.html"


class MyPasswordResetFromKeyView(allauth_views.PasswordResetFromKeyView):
    template_name = "password_reset_from_key.html"
    # success_url = reverse_lazy('profile:edit')


class MyPasswordResetFromKeyDoneView(allauth_views.PasswordResetFromKeyDoneView):
    template_name = "password_reset_from_key_done.html"
