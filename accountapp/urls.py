from django.urls import path
from . import views
from .views import admin_dashboard

urlpatterns = [
    path('', views.landing, name='landing'),
    path('user/signup/', views.user_signup, name='user_signup'),
    path('user/login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/signup/', views.admin_signup, name='admin_signup'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

]
