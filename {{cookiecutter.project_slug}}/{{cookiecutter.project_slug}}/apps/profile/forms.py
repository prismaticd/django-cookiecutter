from django import forms
from django.contrib.auth.models import User
from django.forms import BaseModelFormSet

from .models import Profile


class BaseUserFormSet(BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        user = kwargs["form_kwargs"].pop("user")
        super(BaseUserFormSet, self).__init__(*args, **kwargs)
        self.queryset = User.objects.filter(id=user.id)

    def clean(self):
        super(BaseUserFormSet, self).clean()
        if any(self.errors):
            return
        data = self.forms[0].cleaned_data
        if (
            data["first_name"] is None
            or data["first_name"] == ""
            or data["last_name"] is None
            or data["last_name"] == ""
        ):
            raise forms.ValidationError("Please fill first name and last name")


class BaseProfileFormSet(BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        user = kwargs["form_kwargs"].pop("user")
        super(BaseProfileFormSet, self).__init__(*args, **kwargs)
        self.queryset = Profile.objects.filter(user=user)
        for form in self.forms:
            form.empty_permitted = False
