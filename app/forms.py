from django import forms
from .models import Professor

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['fname', 'lname', 'doj', 'contact']
