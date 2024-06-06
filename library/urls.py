from django.urls import path
from django.http import HttpResponse
from library.views import home, about

urlpatterns = [path("", home), path("about/", about)]
