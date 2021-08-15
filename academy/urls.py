from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('login/', views.login_me),
    path('logout/', views.logout_me),
    path('form-registration/', views.form_registration),
    path('', views.landing, name='index'),
]
