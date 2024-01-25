from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-field', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-field', 'placeholder': 'Your Email Address'}),
            'subject': forms.TextInput(attrs={'class': 'custom-field', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'custom-field', 'placeholder': 'Enter message'}),
        }