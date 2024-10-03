from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('students/', views.students, name='students'),
    path('students/dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('testing/', views.testing, name='testing')
]