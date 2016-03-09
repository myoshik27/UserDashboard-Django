from django import forms
from apps.users.models import CustomUser, Message, Comment

class UserCreationForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

	class Meta:
		model = CustomUser
		fields = ('email', 'first_name', 'last_name', 'description')

	def clean_password2(self):
		# check that the password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise formsl.ValidationError("Passwords do not match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description'}))

	class Meta:
		model = CustomUser
		fields = ('email', 'first_name', 'last_name', 'description')

class AdminUserChangeForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description'}))
	is_superuser = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
	is_active = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
	is_staff = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

	class Meta:
		model = CustomUser
		fields = ('email', 'first_name', 'last_name', 'description', 'is_superuser', 'is_active', 'is_staff',)

class MessageCreationForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something...', 'rows': 3}))

	class Meta(object):
		model = Message
		fields = ('message',)

class CommentCreationForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a comment...', 'rows': 2}))
	message = forms.CharField(widget=forms.HiddenInput())

	class Meta(object):
		model = Comment
		fields = ('comment',)
