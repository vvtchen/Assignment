from django.urls import path
from . import views

urlpatterns = [
    path("createNew", views.createNew, name="createNew"),
    path("all", views.all, name="all"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("templateCreate", views.templateCreate, name="templateCreate"),
    
]