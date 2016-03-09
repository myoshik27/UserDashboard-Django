from django.shortcuts import render, redirect
from django.core import serializers
from django.views.generic import View
from apps.users.forms import UserCreationForm, UserChangeForm, AdminUserChangeForm, MessageCreationForm, CommentCreationForm
from apps.users.models import CustomUser, Message, Comment

class NewUserView(View):
	def get(self,request):
		form = UserCreationForm()
		return render(request, 'users/new.html', {'form': form})
	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print "form is valid"
			form.save()
			return redirect('/dashboard/')
		errors = form.errors
		return render(request, "users/new.html", {'form': form, 'errors': errors})

class UpdateUserView(View):
	def get(self,request):
		# update own information
		# if user is superuser, send them superuser form
		# if user is not superuser, send them regular form
		user = CustomUser.objects.get(id=request.user.id)
		data = user.to_dictionary()
		if request.user.is_superuser:
			form = AdminUserChangeForm(initial=data)
		else:
			form = UserChangeForm(initial=data)
		return render(request, 'users/edit.html', {'form': form})
	def post(self, request):
		print request.POST
		if request.user.is_superuser:
			form = AdminUserChangeForm(request.POST, instance=request.user)
		else:
			form = UserChangeForm(request.POST, instance=request.user)
		print 'Is the form valid?', form.is_valid()
		if form.is_valid():
			user = form.save(commit=False)
			print user.get_full_name() + ': ' + user.description
			user.save()
			return redirect('/dashboard/')
		print form.errors
		errors = "There were errors in the update"
		return render(request, 'users/edit.html', {'form':form,'errors':errors})

class AdminUpdateUserView(View):
	def get(self,request, user_id):
		if not request.user.is_superuser:
			return redirect('/users/edit')
		user = CustomUser.objects.get(id=user_id)
		data = user.to_dictionary()
		form = AdminUserChangeForm(initial=data)
		return render(request, 'users/admin-edit.html', {'form':form, 'user':user})
	def post(self, request, user_id):
		print request.POST
		user = CustomUser.objects.get(id=user_id)
		form = AdminUserChangeForm(request.POST, instance=user)
		print 'Is the form valid?', form.is_valid()
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('/dashboard/')
		print form.errors
		errors = "There were errors in the update"
		return render(request, 'users/admin-edit.html', {'form':form,'errors':errors, 'user': user})

class ShowUserView(View):
	def get(self, request, user_id):
		try:
			user = CustomUser.objects.get(id=user_id)
		except:
			return redirect('/dashboard/')
		messageForm = MessageCreationForm()
		commentForm = CommentCreationForm()
		messages = Message.objects.all().filter(recepient=user_id).order_by('-created_at')
		comments = {}
		for message in messages:
			comments[message.id] = message.comment_set.filter(message=message.id)
		return render(request, 'users/show.html',{'user': user, 'messageForm':messageForm,'commentForm': commentForm, 'messages': messages, 'comments':comments})
	def post(self, request, user_id):
		if 'message-submit' in request.POST:
			form = MessageCreationForm(request.POST)
			if form.is_valid():
				message = form.save(commit=False)
				message.sender = CustomUser.objects.get(id=request.user.id)
				message.recepient = CustomUser.objects.get(id=user_id)
				message.save()
				return redirect('show-user', user_id = user_id)
			errors = form.errors
			print errors
			return redirect('show-user', user_id = user_id)
		elif 'comment-submit' in request.POST:
			form = CommentCreationForm(request.POST)
			print form.is_valid()
			if form.is_valid():
				comment = form.save(commit=False)
				comment.user = CustomUser.objects.get(id=request.user.id)
				comment.message = Message.objects.get(id=request.POST['message'])
				comment.save()
				return redirect('show-user', user_id = user_id)
			errors = form.errors
			return redirect('show-user', user_id = user_id)
		else:
			return redirect('show-user', user_id = user_id)