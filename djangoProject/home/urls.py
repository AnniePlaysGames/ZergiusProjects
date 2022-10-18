from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("home/", views.mybesthome),
    path('person/', views.get_all_persons),
]
