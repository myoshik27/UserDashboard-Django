from django.shortcuts import render, redirect
from django.views.generic import View
from apps.users.models import CustomUser
class DashboardView(View):
	def get(self,request):
		# if loggedin user is a superuser direct them to admin dashboard
		if request.user.is_superuser:
			return redirect('/dashboard/admin')
		users = CustomUser.objects.all()
		return render(request, 'dashboard/dashboard.html',{'users': users})

class AdminDashboardView(View):
	def get(self, request):
		# if loggedin user is not a superuser, direct them to regular dashboard
		# still need to block off non logged in users
		if not request.user.is_superuser:
			return redirect('/dashboard/')
		users = CustomUser.objects.all()
		return render(request, 'dashboard/admin-dashboard.html', {'users': users})