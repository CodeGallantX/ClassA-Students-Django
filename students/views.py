from django.http import HttpResponse
from django.template import loader
from .models import Student

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
  template = loader.get_template('testing.html')
  context = {
    'greeting': 1,
  }
  return HttpResponse(template.render())     