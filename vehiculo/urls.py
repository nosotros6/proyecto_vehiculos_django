from django.urls import path 

# Local
from .views import IndexPageView, vehiculoform_view, navbarView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('vehiculo/add/', vehiculoform_view, name='vehiculo-add'),
    path('navbar/', navbarView, name='navbar'),
]
