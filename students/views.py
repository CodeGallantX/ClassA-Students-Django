from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Student
# from django.db.models import Q
import datetime

def students(request):
  students = Student.objects.all().values()
  template = loader.get_template('students/all_students.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))
  
def dashboard(request, id):
  student = Student.objects.get(id=id)
  today = datetime.datetime.now().date()
  template = loader.get_template('students/dashboard.html')
  context = {
    'student': student,
    'today': today,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('students/index.html')
  return HttpResponse(template.render())

def testing(request):
  data = Student.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('testing.html')
  context = {
    "data": data,
  }
  return HttpResponse(template.render(context, request))     


def add_student(request):
  if request.method == 'POST':
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    date_joined = request.POST['date_joined']
    student = Student(firstname = firstname, lastname = lastname, phone_number = phone_number, email = email, date_joined = date_joined)
    student.save()
    return redirect(success)
  return render(request, 'students/forms.html')


# def remove_student(request, id):
#   del_student = Student.objects.get(id=id)
#   del_student.delete()
#   template = loader.get_template('students/delete_student')
#   return HttpResponse(success)


def success(request):
  template = loader.get_template('success.html')
  # success_icon = "bi bi-check-circle-fill"
  # context = {
  #   'success_icon': success_icon,
  # }
  return HttpResponse(template.render())