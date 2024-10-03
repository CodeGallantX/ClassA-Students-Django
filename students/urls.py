from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),
]