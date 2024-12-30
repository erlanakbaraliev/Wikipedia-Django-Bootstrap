from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("/search/", views.search, name="search"),
    path("/newPage/", views.newPage, name="newPage"),
    path("/edit/", views.edit, name="edit"),
    path("/edit/save_edit/", views.save_edit, name="save_edit")
]
