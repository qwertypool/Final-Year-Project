from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_view(request):
    return render(request, 'home/home.html')


def about_view(request):
    return render(request, 'home/about.html')
    
def faq(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')
    return render(request, 'faqs.html')



#@login_required(redirect_field_name='userlogin')
def contact_view(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')       
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(phone) < 10 or len(content) < 2:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, "Your Query has been sent!")
    return render(request, 'home/contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Validations for inputs
        if len(username) > 15:
            messages.error(
                request, "Length of username should be less than 15")
            return redirect('home')
        if len(username) < 3:
            messages.error(
                request, "Length of username must be greater than 3")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Symbols not allowed")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords did not matched!")
            return redirect('home')
        if len(phone) < 9 or phone.isalpha():
            messages.error(request, "Invalid Phone number")
            return redirect('home')
        # creating user
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect('home')

    else:
        return HttpResponse('404 Not Found')

def login_view(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('home')
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    messages.success(request,"You have been successfully logged out!")
    return redirect('home')
   

