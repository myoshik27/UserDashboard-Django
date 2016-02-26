from django.shortcuts import render
from django.views.generic import View

class NewUserView(View):
	def get(self,request):
		return render(request, 'users/new.html')

class UpdateUserView(View):
	def get(self,request):
		return render(request, 'users/edit.html')