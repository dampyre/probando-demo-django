from django import forms
# formulario de contacto
class ContactForm(forms.Form):
		email		= forms.EmailField(widget=forms.TextInput())
		titulo		= forms.CharField(widget=forms.TextInput())
		texto 		= forms.CharField(widget=forms.Textarea())
# formulario login
class LoginForm(forms.Form):
		username = forms.CharField(widget=forms.TextInput())
		password = forms.CharField(widget=forms.PasswordInput(render_value=False))

