from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students/dashboard/<int:id>/', views.dashboard, name='dashboard'),
]