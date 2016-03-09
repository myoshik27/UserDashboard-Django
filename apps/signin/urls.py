from django.conf.urls import patterns, url
from apps.signin import views

urlpatterns = patterns('',
	url(r'^$', views.SigninView.as_view(), name="signin"),
	url(r'^logout/', views.LogoutView.as_view(), name="logout"),
)