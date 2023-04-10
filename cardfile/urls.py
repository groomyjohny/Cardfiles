from django.contrib import admin
from django.urls import path

import cardfile.views

appname = "cardfile"

urlpatterns = [
    path('', cardfile.views.index, name="index"),
]
