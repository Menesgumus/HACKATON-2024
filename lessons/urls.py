from django.urls import path
from . import views

urlpatterns = [
    path("makine-muhendisligi", views.machine),
    path("yazilim-muhendisligi", views.software),
    path("elektrik-ve-elektronik-muhendisligi", views.electronic),
    path("bilgisayar-muhendisligi", views.computer),
    path("endustri-muhendisligi", views.endustry),
    path("gida-muhendisligi", views.food),
    path("insaat-muhendisligi", views.construction),
    
    path("tip", views.medicine),
    path("dis-hekimligi", views.tooth),
    path("hemsirelik", views.nurse),
    path("eczacilik", views.pharmacy),
    path("veterinerlik", views.veterinary),
]