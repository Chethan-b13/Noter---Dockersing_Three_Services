from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',home),
    path('login',login),
    path('signup',signup),
    path('notes',notes),
    path('flaskpp',RedirectView.as_view(url='flask:5030'),name='flaskapp'),
]