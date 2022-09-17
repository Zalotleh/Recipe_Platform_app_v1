from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .constants import COUNTRIES_CHOICES
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))


class UpdateUserForm(ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website_url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}))
    facebook_url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}))
    twitter_url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}))
    instagram_url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}))
    pinterest_url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}))

    country_of_origin = forms.RadioSelect(choices=COUNTRIES_CHOICES)
    biography = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "website_url", "facebook_url", "twitter_url", "instagram_url",
                  "pinterest_url", "country_of_origin", "biography", "avatar"]
