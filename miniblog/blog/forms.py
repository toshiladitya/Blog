from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm , UsernameField
from django.contrib.auth.models import User 
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post
class Signup(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
     model = User
     fields=['username','first_name','last_name','email']
     labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
     
     widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
              'first_name':forms.TextInput(attrs={'class':'form-control'}),
              'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
              }
     
class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True }))
    password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'currentpassword','class':'form-control'}))
    

class PostForm(forms.ModelForm):
    
    class Meta:
        model =Post 
        fields =['title','desc']
        lables={'title':'Tiltle','desc':'Description'}
        widgets={ 'title':forms.TextInput(attrs={'class':'form-control'}),
                  'desc':forms.Textarea(attrs={'class':'form-control'})  
        } 