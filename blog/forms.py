from django import forms
from .models import ClientMessage

class ClientMessageForm(forms.ModelForm):
    class Meta:
        model = ClientMessage
        fields = ['name', 'email', 'company', 'phone_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' ', 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' ', 'id': 'id_email'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' ', 'id': 'id_company'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' ', 'id': 'id_phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' ', 'id': 'id_message', 'rows': 10}),
        }