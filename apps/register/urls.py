from django.conf.urls import patterns, url
from apps.register.views import RegisterView

urlpatterns = patterns('',
	url(r'^$', RegisterView.as_view()),
)