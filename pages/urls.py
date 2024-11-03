from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("iletisim", views.contact),
    path("egitim", views.education),
    path("hakkimizda", views.about),
]
