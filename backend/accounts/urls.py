from django.urls import path
from .views import SignupView, getCSRFToken

urlpatterns = [
    path("register", SignupView.as_view()),
    path("csrf_cookie", getCSRFToken.as_view()),
]
