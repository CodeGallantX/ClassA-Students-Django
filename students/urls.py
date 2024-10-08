from django.urls import path
from . import views
# from .views import AddStudentView

urlpatterns = [
    path('', views.main, name="main"),
    path('students/', views.students, name='students'),
    path('students/dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('students/add_student/', views.add_student, name="add_student"),
    path('students/update/', views.update, name="update"),
    path('students/update/<int:id>', views.update_student, name="update_student"),
    path('students/delete/<int:id>', views.delete, name="delete"),
    # path('add_student/', AddStudentView.as_view(), name="add_student"),
    path('success/<str:action_type>/', views.message, name='success'),
    path('testing/', views.testing, name='testing'),
]