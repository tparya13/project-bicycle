from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def registerUser(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        print(fname,lname,email,username,password,cpassword)
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('auth:register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('auth:register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                return redirect('auth:login')
        else:
            messages.info(req,"password not matched")
            return redirect('auth:register')
    return render(req, 'registeruser.html')
def loginUser(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        # print(user)
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect('shop:home')
        else:
            messages.info(req, "invalidcredentials")
            return redirect('auth:login')
       
    return render(req, 'loginuser.html')


def logoutUser(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('shop:home')