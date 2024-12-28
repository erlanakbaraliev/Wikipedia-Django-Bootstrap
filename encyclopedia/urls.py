from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:name>", views.displayPage, name="displayPage"),
    path("wiki/createNewPage/", views.createNewPage, name="createNewPage"),
]
