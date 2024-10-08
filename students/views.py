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
      return redirect(message, action_type='add')
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


def delete(request, id):
  student = Student.objects.get(id=id)
  if request.method == 'POST':
    try:
      student.delete()
      student.save()
      return redirect(message, action_type='delete')
    except Student.DoesNotExist:
      return redirect(message, action_type='error')
  template = loader.get_template('students/delete.html')
  return HttpResponse(template.render())

def delete_student(request, id):
  student = Student.objects.get(id=id)
  if request.method == 'POST':
    try:
      student.delete()
      student.save()
      return redirect(message, action_type='delete')
    except Student.DoesNotExist:
      return redirect(message, action_type='error')
  template = loader.get_template('students/delete.html')
  return HttpResponse(template.render())


def update(request):
  if request.method == 'POST':
    id = request.POST['id']
    try:
      student = Student.objects.get(id=id)
      return redirect(update_student, id=id)
    except Student.DoesNotExist:
      return redirect(message, action_type='error')
  template = loader.get_template('students/update.html')
  return HttpResponse(template.render({}, request))

def update_student(request, id):
  student = Student.objects.get(id=id)
  if request.method == 'POST':
    student.firstname = request.POST['firstname']
    student.lastname = request.POST['lastname']
    student.phone_number = request.POST['phone_number']
    student.email = request.POST['email']
    student.save()
    return redirect(message, action_type='update')
  template = loader.get_template('students/update_form.html')
  context = {
    'student': student,
  }
  return HttpResponse(template.render(context, request))


def message(request, action_type):
  template = loader.get_template('success.html')
  if action_type == 'add':
    message = "<strong>Success!</strong> You have successfully add a student."
    is_error = False
  elif action_type == 'update':
    message = "<strong>Success!</strong> You have successfully updated the student record."
    is_error = False
  elif action_type == 'update':
    message = "<strong>Success!</strong> The student record has been successfully deleted."
    is_error = False
  elif action_type == 'error':
    message = "<strong>&#x26A0; Oops</strong> No student with that ID exists."
    is_error = True
  else:
    message = "<strong>Success!</strong> Operation completed successfully."
    is_error = False
  context = {
    "message": message,
    "is_error": is_error,
  }
  return HttpResponse(template.render(context, request))