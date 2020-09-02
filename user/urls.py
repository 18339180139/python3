from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login),
    path('login_logic/', views.login_logic),
]