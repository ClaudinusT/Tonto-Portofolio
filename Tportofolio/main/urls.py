from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("contact/", views.contact, name='contact'),
    path("project/<int:id>/", views.projectDetail, name='projectDetail'), #specifying the project detail id
]
