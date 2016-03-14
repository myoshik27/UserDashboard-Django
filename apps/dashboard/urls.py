from django.conf.urls import patterns, url
from apps.dashboard.views import DashboardView, AdminDashboardView

urlpatterns = patterns('',
	# since we are using class-based views, we need to use the .as_view() function
	url(r'^$', DashboardView.as_view(), name='show-dashboard'),
	url(r'^admin/', AdminDashboardView.as_view(), name='show-admin-dashboard'),
)

