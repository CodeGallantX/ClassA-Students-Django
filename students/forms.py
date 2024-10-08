from django import forms
from .models import Student 

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        # def __init__(self, *args, **kwargs):
        #     super(AddStudentForm, self).__init__(*args, **kwargs)
        #     self.fields['firstname'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        #     self.fields['lastname'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        #     self.fields['phone_number'].widget = forms.NumberInput(attrs={'readonly':'readonly'})
        #     self.fields['email'].widget = forms.EmailInput(attrs={'readonly':'readonly'})