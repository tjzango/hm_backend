from django.urls import path
from .views import homepage_view

urlpatterns = [
    path('hello/', homepage_view, name='hello'),
]





