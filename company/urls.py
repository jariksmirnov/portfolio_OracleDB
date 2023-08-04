from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
    path('', views.companies, name='companies'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/detail_taxes/', views.detail_taxes, name='detail_taxes'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
