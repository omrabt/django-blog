from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name'
                }
            ),
               'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email Adress'
                }
            ),
               'phone': forms.TextInput(
                attrs={
                    'placeholder': 'phone'
                }
            ),
               'messages': forms.TextInput(
                attrs={
                    'placeholder': 'messages'
                }
            ),
        }