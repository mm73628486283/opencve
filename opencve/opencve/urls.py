from django.contrib import admin
from django.urls import include, path

from core.views import CweView, HomeView
from users.views import register, CustomLoginView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("admin/", admin.site.urls),
    path("cwe/", CweView.as_view()),
    path("accounts/", include("users.urls")),
]
