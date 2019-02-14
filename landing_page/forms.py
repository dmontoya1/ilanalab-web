from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'John Doe'}
    ), min_length=3, max_length=50)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': 'my@email.com'}
    ), min_length=3, max_length=100)
    celular = forms.CharField(label="Celular", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': '3332211000'}
    ), min_length=3, max_length=10)
