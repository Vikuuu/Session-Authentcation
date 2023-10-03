from django.urls import path
from .views import SignupView, getCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, GetUserView

urlpatterns = [
    path("authenticated", CheckAuthenticatedView.as_view()),
    path("register", SignupView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogoutView.as_view()),
    path("csrf_cookie", getCSRFToken.as_view()),
    path("delete", DeleteAccountView.as_view()),
    path("getusers", GetUserView.as_view()),
]
