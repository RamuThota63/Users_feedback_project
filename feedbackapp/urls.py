from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback'),
    path('thankyou/<int:feedback_id>/', views.thank_you, name='thank_you'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
]
