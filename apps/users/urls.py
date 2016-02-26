from django.conf.urls import patterns, url
from apps.users.views import NewUserView, UpdateUserView

urlpatterns = patterns('',
	url(r'^new/', NewUserView.as_view()),
	url(r'^update/', UpdateUserView.as_view()),
)

