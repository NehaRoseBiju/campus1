from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit_request, name='submit_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('request/<int:pk>/edit/', views.edit_request, name='edit_request'),
    path('request/<int:pk>/delete/', views.delete_request, name='delete_request'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/update/<int:pk>/', views.staff_update_status, name='staff_update_status'),
]
