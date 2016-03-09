from django.conf.urls import patterns, url
from apps.users.views import NewUserView, UpdateUserView, AdminUpdateUserView, ShowUserView

urlpatterns = patterns('',
	url(r'^new/', NewUserView.as_view(), name="admin-create-user"),
	url(r'^edit/$', UpdateUserView.as_view(), name='edit-user'),
	url(r'^edit/(?P<user_id>\d+)/$', AdminUpdateUserView.as_view(), name='admin-edit-user'),
	url(r'^show/(?P<user_id>\d+)/$', ShowUserView.as_view(), name='show-user')
)

