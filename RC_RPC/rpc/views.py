from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import details
from django.core.validators import validate_email
from django.contrib.auth import login ,logout ,authenticate
import re
from django.http import HttpResponse


def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        user_regex='^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)$'
        email_regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        flag=0
        data=request.POST
        username=data['username']
        f_name=data['fname']
        l_name=data['lname']
        email=data['email']
        ph_no=data['mob']
        password = data['password1']

        if(re.search(user_regex,username)==None):
            messages.info(request,"Invalid username, Please enter valid username")
            flag=1
        if(f_name.isalpha()==False):
            messages.info(request,"Invalid first name, Please enter valid first name")
            flag=1
        if(l_name.isalpha()==False):
            messages.info(request,"Invalid last name, Please enter valid last name")
            flag=1
        if(re.search(email_regex,email)==None):
            messages.info(request,"Invalid mail id, enter correct email id!!")
            flag=1
        if(ph_no.isdigit()==False) or (len(str(ph_no))!=10) or (str(ph_no)[0] in ['0','1','2','3','4','5']):
            messages.info(request,"Invalid phone number, Please enter valid phone number")
            flag=1
        if flag==1:
            return render(redirect('rpc/signup.html'))
        else:
            if data['password1']==data['password2']:
                try:
                    user=User.objects.create_user(username=username,first_name=f_name,last_name=l_name,email=email,password=password)
                    profile=details(user=user,ph_no=ph_no)
                    profile.save()
                    user = auth.authenticate(username=username,password=password)
                    login(request,user)
                    return redirect('success')
                except:
                    messages.info(request,'User already exist, please try another one')
                    return render(request,'rpc/signup.html',)

            messages.info(request, 'Passwords do not match, try again')
            return render(request,'rpc/signup.html',)
    if request.method=="GET":
        return render(request,'rpc/signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'rpc/success.html',)
        else:
            messages.info(request,'Invalid Username or password')
            return render(request,'rpc/signin.html',)
    if request.method=="GET":
        return render(request,'rpc/signin.html',)

def success(request):
    data=details.objects.get(user=request.user)
    return render(request,'rpc/success.html',{'data': data})


def signout(request):
    auth.logout(request)
    messages.info(request,'You are logged out successfully!')
    return render(request,'rpc/signin.html')
