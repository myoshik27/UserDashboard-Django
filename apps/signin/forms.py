from django import forms
class SigninForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))