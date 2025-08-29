from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_user, name='login_user'),
]
