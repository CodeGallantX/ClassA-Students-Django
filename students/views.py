from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.db.models import Q

def students(request):
  students = Student.objects.all().values()
  template = loader.get_template('students/all_students.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))
  
def dashboard(request, id):
  student = Student.objects.get(id=id)
  template = loader.get_template('students/dashboard.html')
  context = {
    'student': student,
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