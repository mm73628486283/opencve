from re import I
from django.contrib import admin
from django.urls import path

from core.views import CweView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cwe/", CweView.as_view()),
]
