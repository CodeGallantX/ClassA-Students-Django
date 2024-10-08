from django.urls import path
from . import views
# from .views import AddStudentView

urlpatterns = [
    path('', views.main, name="main"),
    path('students/', views.students, name='students'),
    path('students/dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('students/add_student/', views.add_student, name="add_student"),
    # path('add_student/', AddStudentView.as_view(), name="add_student"),
    path('success/', views.success, name='success'),
    path('testing/', views.testing, name='testing'),
]