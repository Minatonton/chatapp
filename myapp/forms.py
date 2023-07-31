from django import forms
from .models import CustomUser,Talk_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
class form_Customer(UserCreationForm):
   class Meta:
      model = CustomUser
      fields = ('username','email','image')
class loginform(AuthenticationForm):
   class Meta:
      model = CustomUser
      fields=('username','password')      
class logoutform(AuthenticationForm):
   class Meta:
      model = CustomUser
class password_changeform(PasswordChangeForm):
   class Meta:
      model = CustomUser
      fields=('old_password','new_password',)
class Name_changeform(forms.ModelForm):
   class Meta:
      model=CustomUser
      fields=("username",)
class Talk_form(forms.ModelForm):
   class Meta:
      model=Talk_model
      fields = ("message",)
class Email_changeform(forms.ModelForm):
   class Meta:
      model=CustomUser
      fields=("email",)
class Img_changeform(forms.ModelForm):
   class Meta:
      model=CustomUser
      fields=("image",)            

