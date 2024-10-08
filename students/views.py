from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Student
from .forms import AddStudentForm
from django.views.generic import CreateView
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


# def add_student(request):
#   if request.method == 'POST':
#     firstname = request.POST['firstname']
#     lastname = request.POST['lastname']
#     phone_number = request.POST['phone_number']
#     email = request.POST['email']
#     date_joined = request.POST['date_joined']
#     student = Student(firstname = firstname, lastname = lastname, phone_number = phone_number, email = email, date_joined = date_joined)
#     student.save()
#     return redirect(success)
#   return render(request, 'students/forms.html')


def add_student(request):
  template = loader.get_template('students/forms.html')
  if request.method == 'POST':
    form = AddStudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(success)
    else:
      print(form.errors)
  context = {
    "form" : AddStudentForm,
  }
  return HttpResponse(template.render(context, request))


class AddStudentView(CreateView):
  model = Student
  fields = "__all__"
  template_name = 'students/forms.html'
  success_url = '../success'


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