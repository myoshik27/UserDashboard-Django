from django.shortcuts import render, redirect
from django.views.generic import View
from apps.users.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
class RegisterView(View):
	def get(self, request):
		form = UserCreationForm()
		return render(request, "register/register.html", {'form':form})
	def post(self,request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print "form is valid"
			form.save()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user = authenticate(username=email, password=password)
			print 'user', user
			if user is not None:
				login(request, user)
				if user.is_superuser:
					return redirect('/dashboard/admin')
				return redirect('/dashboard/')
		errors = "form has errors"
		return render(request, "register/register.html", {'form': form, 'errors': errors})