from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from  EXM import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return  render(request,"base.html")
def index(request):
    return  render(request,"index.html")

def singup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname'] 
        lname=request.POST['lname'] 
        email=request.POST['email']  
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request," Email already registered")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request,"Username must be unde 10 characters")
        
        if(pass1 !=pass2):
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('index') 
            


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your account has been successfully created.We have sent you a confirmation email .please check your email to  activate your  account ")
        


        #Welcome Email
        subject="Welcome to the EXM-login."
        message="Hello"+myuser.first_name+"!\n"+"Welcome to the EXM\n Thank you for visiting our website \n We have  also sent you a confirmation email,please confirm your email address in order to activate your account.\n\n Thanking you Aaayushi "
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect('singin')
    
    return render(request,"singup.html")



def singin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1'] 
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"index.html",{'fname':fname})
    
        else:
            messages.error(request," Bad Credential")
            return redirect('index')
    return render(request,"singin.html")


def singout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('index')

