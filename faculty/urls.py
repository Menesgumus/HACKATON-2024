from django.urls import path
from . import views

urlpatterns = [
    path("muhendislik-fakultesi", views.engineer),
    path("saglik-fakultesi", views.health),
]
 