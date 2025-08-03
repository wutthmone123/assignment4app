from django import forms
from .models import assignment4app

class StudentForm(forms.ModelForm):
    class Meta:
        model = assignment4app
        fields = ['name', 'email', 'gender', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name......'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Email......'}),
            'gender': forms.Select(attrs={'class': 'form-select','placeholder':'Choose gender'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Phone........'}),
        }
    