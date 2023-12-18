from django.contrib import admin
from django.urls import path, include

from receivefile.views import upload

urlpatterns = [
    path('', upload, name="upload")

]
