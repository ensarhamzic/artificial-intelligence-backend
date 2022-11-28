from django.urls import path
from . import views

urlpatterns = [
    path('get-path', views.getPath),
    path('get-move', views.getMove)
]
