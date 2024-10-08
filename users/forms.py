from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#User Registration form
class UserRegisterForm(UserCreationForm):
	email= forms.EmailField()
	
	class Meta:
		model= User
		fields= ['username', 'email', 'password1','password2']
		
	
#User Update form (email, username)	
class UserUpdateForm(forms.ModelForm):
	
	email= forms.EmailField()
	
	class Meta:
		model= User
		fields= ['username', 'email']
	
#User Update form (Profile)		
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model= Profile
		fields = ['image']
