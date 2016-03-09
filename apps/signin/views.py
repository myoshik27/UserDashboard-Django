from django.shortcuts import render, redirect
from django.views.generic import View
from apps.signin.forms import SigninForm
from django.contrib.auth import login, authenticate, logout
class SigninView(View):
	def get(self,request):
		form = SigninForm()
		return render(request, 'Signin/signin.html', {'form': form})
	def post(self,request):
		form = SigninForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				if user.is_superuser:
					return redirect('/dashboard/admin')
				return redirect('/dashboard/')
		error = "Invalid Login"
		return render(request, 'Signin/signin.html', {'form': form, 'error': error})

class LogoutView(View):
	def get(self,request):
		print "logging out"
		logout(request)
		return redirect('/')