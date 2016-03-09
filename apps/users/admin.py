from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.users.forms import UserChangeForm, UserCreationForm
from apps.users.models import CustomUser, Message, Comment
# Register your models here.

class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserChangeForm
	add_form = UserCreationForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User
	list_display = ('email', 'first_name', 'last_name', 'is_superuser', 'is_staff')
	# list_filter = ('is_staff', 'is_superuser', 'is_active')
	fieldsets = (
		(None, {'fields': ('email','password',)}),
		('Personal info', {'fields': ('first_name','last_name','description')}),
		('Permissions', {'fields': ('is_superuser','is_staff')}),
		('Active', {'fields': ('is_active',)})
	)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields': ('email', 'first_name','last_name', 'description', 'password1', 'password2')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

# Now register the new UserAdmin
admin.site.register(CustomUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin
admin.site.unregister(Group)
admin.site.register(Message)
admin.site.register(Comment)