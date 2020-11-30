from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.index),
    path("process", views.process),
    path("shows", views.shows),
    path("shows/<int:show_id>",views.all_shows),
    path("edit_shows/<int:show_id>",views.edit_shows),
    path("process_edit_shows/<int:show_id>", views.process_edit_shows),
    path("destroy", views.destroy)

]
