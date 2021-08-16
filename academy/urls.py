from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('login/', views.login_me),
    path('logout/', views.logout_me),
    path('register-user/', views.register_user),
    path('form-registration/', views.form_registration),
    path('class-register/', views.register_class),
    path('', views.landing, name='index'),
]
