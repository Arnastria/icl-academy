from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/<int:id_branch>/', views.dashboard),
    path('login/', views.login_me),
    path('logout/', views.logout_me),
    path('detail-kelas/<int:id_kelas>/', views.detail_kelas),
    path('register-user/', views.register_user),
    path('form-registration/', views.form_registration),
    path('class-register/', views.register_class),
    path('', views.landing, name='index'),
]
