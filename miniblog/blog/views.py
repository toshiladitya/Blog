from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Signup,Loginform ,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})



def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')




def dashboard(request):
      if request.user.is_authenticated:
          posts=Post.objects.all()
          user=request.user
          full_name= user.get_full_name()
          gps=user.groups.all()
          return render(request,'dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
      else:
        return render(request,'dashboard.html')



def user_signup(request):
    if request.method == 'POST':  
     form=Signup(request.POST)
     if form.is_valid():
        messages.success(request,"Congratulations You Have Become An Author")
        user=form.save()
        group=Group.objects.get(name='Author')
        user.groups.add(group)
        
        return HttpResponseRedirect('/login/')
    else:
        form=Signup()
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if  not request.user.is_authenticated:
        if request.method=='POST':
            form=Loginform(request=request,data=request.POST)
            if form.is_valid():
              uname=form.cleaned_data['username']
              upass=form.cleaned_data['password'] 
              user=authenticate(username=uname,password=upass)
              if user is not None:
                login(request,user)
                messages.success(request,"Logged In Successfully !!")
                return HttpResponseRedirect('/dashboard/')
            
        else:
            form=Loginform()
        return render(request,'logins.html',{'form':form})
                
    else:
        return HttpResponseRedirect('/dashboard/')       

def contact(request):
    return render(request,'contact.html')

def Addnewpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
         form=PostForm(request.POST)
         if form.is_valid():
             title=form.cleaned_data['title']
             desc=form.cleaned_data['desc']
             pst=Post(title=title,desc=desc)
             pst.save()
             form=PostForm()
        else:
            form=PostForm()
        return render(request,'addpost.html',{'form':form})
        
    else:
        return HttpResponseRedirect('/login/')
    
def Updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST , instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render (request,'updatepost.html',{'form':form})
    
    else:
        return HttpResponseRedirect('/login/')
    
    
def Deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/lo gin/')        
    