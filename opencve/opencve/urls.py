from django.contrib import admin
from django.urls import include, path

from core.views import CweView, HomeView
from users.views import register, CustomLoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("welcome/", HomeView.as_view(), name="welcome"),
    path("register/", register, name="register"),
    path("accounts/", include("users.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("admin/", admin.site.urls),
    path("cwe/", CweView.as_view()),
]
