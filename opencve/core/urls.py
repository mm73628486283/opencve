from django.urls import path

from core.views import CweView, HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cwe/", CweView.as_view(), name="cwe"),
]
