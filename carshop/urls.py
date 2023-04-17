from django.urls import path

from . import views

app_name = "carshop"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
]