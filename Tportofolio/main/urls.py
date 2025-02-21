from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='content'),
    path("home/", views.home, name='content'),
    path("contact/", views.contact, name='contact'),
    path("project/<int:id>/", views.projectDetail, name='projectDetail'), #specifying the project detail id
]
