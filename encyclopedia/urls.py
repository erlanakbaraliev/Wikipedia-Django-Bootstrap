from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.displayPage, name="displayPage"),
    path("wiki/<str:name>/edit", views.edit, name="edit"),
    path("wiki/createNewPage/", views.createNewPage, name="createNewPage"),
    path("search", views.search, name="search"),
]
