# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

import logging

logger = logging.getLogger(__name__)


class AuthApp(object):
    name = "myauth_app"

    def get_urls(self):
        urlpatterns = [
            url(r"^login/$", views.MyLoginView.as_view(), {"template_name": "login.html"}, name="account_login"),
            url(r"^logout/$", auth_views.logout, name="account_logout"),
            url(
                r"^register/$", views.MySignupView.as_view(), {"template_name": "register.html"}, name="account_signup"
            ),
            url(r"^email/change/$", views.MyEmailView.as_view(), name="account_email"),
            url(r"^email/confirm/(?P<key>[-:\w]+)/$", views.MyConfirmEmailView.as_view(), name="account_confirm_email"),
            url(r"^password/change/$", views.MyPasswordChangeView.as_view(), name="account_change_password"),
            url(r"^password/set/$", views.MyPasswordSetView.as_view(), name="account_set_password"),
            url(r"^password/reset/$", views.MyPasswordResetView.as_view(), name="password_reset"),
            url(r"^password/reset/done/$", views.MyPasswordResetDoneView.as_view(), name="account_reset_password_done"),
            url(
                r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
                views.MyPasswordResetFromKeyView.as_view(),
                name="account_reset_password_from_key",
            ),
            url(
                r"^password/reset/key/done/$",
                views.MyPasswordResetFromKeyDoneView.as_view(),
                name="account_reset_password_from_key_done",
            ),
            url(r"^accounts/", include("allauth.socialaccount.providers.google.urls")),
            url(r"^accounts/", include("allauth.socialaccount.providers.facebook.urls")),
        ]

        return urlpatterns

    @property
    def urls(self):
        # no namespace for compatibility with django-allauth
        return self.get_urls(), self.name, ""


myauth = AuthApp()
