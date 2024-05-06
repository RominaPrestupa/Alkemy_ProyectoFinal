from django.urls import path
from .views import login_view, logout_view

# vistas de usuario
urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
]