from django.urls import path
# Local
from .views import registro_view, login_view


urlpatterns = [
    path('registro/', registro_view, name="registro"),
    path('login/', login_view, name="login"),
]  