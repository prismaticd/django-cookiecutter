from allauth.socialaccount.views import ConnectionsView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import modelformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import BaseUserFormSet, BaseProfileFormSet
from .models import Profile


class ProfileEditView(LoginRequiredMixin, ConnectionsView):
    pass


class ProfileView(ProfileEditView):
    template_name = "profile.html"
    success_url = reverse_lazy('profile:edit')


class MyProfileView(ProfileView):
    template_name = 'profile.html'
    success_url = reverse_lazy('profile:edit')

    ProfileFormSet = modelformset_factory(Profile, extra=0, formset=BaseProfileFormSet,
                                          fields=[])
    UserFormSet = modelformset_factory(User, extra=0, formset=BaseUserFormSet, fields=("first_name", "last_name"))

    def get_context_data(self, **kwargs):
        need_validation = False
        try:
            profile = self.request.user.profile
        except ObjectDoesNotExist:
            Profile.objects.create(user=self.request.user)

        context = super(MyProfileView, self).get_context_data(**kwargs)
        context['user_formset'] = self.UserFormSet(form_kwargs={'user': self.request.user}, prefix="user_formset")
        context['profile_formset'] = self.ProfileFormSet(form_kwargs={'user': self.request.user},
                                                         prefix="profile_formset")
        context['need_validation'] = need_validation
        return context

    def post(self, request, *args, **kwargs):
        user_formset = self.UserFormSet(request.POST, prefix="user_formset", form_kwargs={'user': self.request.user})
        profile_formset = self.ProfileFormSet(request.POST, prefix="profile_formset",
                                              form_kwargs={'user': self.request.user})
        if user_formset.is_valid() and profile_formset.is_valid():
            user_formset.save()
            profile_formset.save()
        return render(request, "profile.html",
                      {'user_formset': user_formset, 'profile_formset': profile_formset})