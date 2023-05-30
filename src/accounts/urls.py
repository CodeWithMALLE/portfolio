from django.urls import path

from src.accounts.views import login_user, signup, logout_user

app_name = "accounts"
urlpatterns = [
	path("login/", login_user, name="login_user"),
	path("signup/", signup, name="signup"),
	path("logout/", logout_user, name="logout_user"),
]
