from django.shortcuts import render, redirect
from django.views.generic import View
from apps.users.models import CustomUser
class DashboardView(View):
	def get(self,request):
		if request.user.is_superuser:
			return redirect('/dashboard/admin')
		users = CustomUser.objects.all()
		return render(request, 'dashboard/dashboard.html',{'users': users})

class AdminDashboardView(View):
	def get(self, request):
		if not request.user.is_superuser:
			return redirect('/dashboard/')
		users = CustomUser.objects.all()
		return render(request, 'dashboard/admin-dashboard.html', {'users': users})