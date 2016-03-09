from django.conf.urls import patterns, url
from apps.dashboard.views import DashboardView, AdminDashboardView

urlpatterns = patterns('',
	url(r'^$', DashboardView.as_view(), name='show-dashboard'),
	url(r'^admin/', AdminDashboardView.as_view(), name='show-admin-dashboard'),
)

