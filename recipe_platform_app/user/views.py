# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm


class LoginUser(LoginView):
    template_name = "user_login.html"


class ChangePassword(SuccessMessageMixin,PasswordChangeView):
    template_name = "password_change.html"
    success_message = "Your password is changed successfully"
    success_url = reverse_lazy("home_page")


class RegisterUser(View):
    template_name = "user_registration.html"
    form_class = SignUpForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() or profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile is updated")
            return redirect(to="user:user_profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, "user_profile.html", {"user_form": user_form, "profile_form": profile_form})
