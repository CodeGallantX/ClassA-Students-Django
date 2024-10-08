from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'email', 'date_joined')
    search_fields = ('firstname', 'lastname', 'phone_number', 'email',)


admin.site.register(Student, StudentAdmin)