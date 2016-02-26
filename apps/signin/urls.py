from django.conf.urls import patterns, url
from apps.signin.views import SigninView

urlpatterns = patterns('',
	url(r'^$', SigninView.as_view()),
)