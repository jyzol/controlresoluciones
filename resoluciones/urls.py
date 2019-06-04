from django.urls import path

from .views import home, resolucion_list

urlpatterns = [
    path('home', resolucion_list),
]