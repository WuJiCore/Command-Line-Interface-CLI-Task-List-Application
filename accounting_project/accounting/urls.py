from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('add_sale/', views.add_sale, name='add_sale'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('view_data/', views.view_data, name='view_data'),
    path('request_edit/<str:model_name>/<int:object_id>/', views.request_edit, name='request_edit'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('deny_request/<int:request_id>/', views.deny_request, name='deny_request'),
]
