from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import LoginUser, ChangePassword, RegisterUser, profile

app_name = "user"
urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("changepassword/", ChangePassword.as_view(), name="password_change"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile, name="user_profile")
]
