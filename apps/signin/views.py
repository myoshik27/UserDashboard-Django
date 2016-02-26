from django.shortcuts import render
from django.views.generic import View
from apps.signin.forms import SigninForm
class SigninView(View):
	def get(self,request):
		form = SigninForm()
		return render(request, 'Signin/signin.html', {'form': form})
