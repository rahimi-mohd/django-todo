from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.home, name="home"),
    path("change_status/<int:pk>/", views.change_status, name="change_status"),
]