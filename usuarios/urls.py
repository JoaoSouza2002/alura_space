from django.urls import path
from galeria.views import index, imagem, buscar
from usuarios.views import login, register

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
]