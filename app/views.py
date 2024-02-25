from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BuyerForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

# Register page 
def Register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phonenumber')
        print(first_name,last_name,email,password,phone_number)
        if len(password) > 10:
            messages.error(request, 'password must be less then 10 character.')
            return redirect('register')
        if len(password) < 8:
            messages.error(request, 'password must be greater than 8 character.')
            return redirect('register')
        if CustomModel.objects.filter(email=email):
            messages.error(request, 'This email is already exit please try other email.')
            return redirect('register')
        reg = CustomModel(first_name=first_name,last_name=last_name, email=email,phonenumber=phone_number)
        reg.set_password(password)
        reg.save()
        messages.success(request, 'You have signed up successfully.')
        return redirect('signin')
    else:
        return render(request, 'register.html')

# Sign in page 
def Sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        if len(password) > 10:
            messages.error(request, 'password must be less then 10 character.')
            return redirect('signin')
        if len(password) < 8:
            messages.error(request, 'password must be greater than 8 character.')
            return redirect('signin')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successully.')
            return redirect('home')
        return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

# Home view 
def home(request):
    return render(request, 'home.html')

# User logout view
@login_required(login_url='signin')
def user_logout(request):
    logout(request)
    return redirect('/')

# Base view
def base(request):
    return render(request, 'base.html')

# Buyer view
@login_required(login_url='signin')
def buyer(request):
    if request.method == 'POST':
        name = request.POST.get('bookname')
        price = request.POST.get('bookprice')
        image = request.FILES.get('myimage')
        reg = Buyer(user=request.user, bookname=name, price=price, image=image)
        reg.save()
        messages.success(request, 'Your book added successfully!')
        return redirect('showbook')
    return render(request, 'buyer.html')

# Seller view
@login_required(login_url='signin')
def seller(request):
        product = Buyer.objects.all()
        context = {'products':product}
        return render(request, 'seller.html', context)

# showbook view
@login_required(login_url='signin')
def showbook(request):
    product = Buyer.objects.filter(user=request.user)
    context = {'products':product}
    return render(request, 'showbook.html', context)

# About page view
@login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')

# Contact view
@login_required(login_url='signin')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')
        print(name,email,address,message)
        reg = Contact(name=name,email=email,address=address,message=message)
        reg.save()
        messages.success(request, 'Thanks for contacting...')
        return redirect('/')
    return render(request, 'contact.html')

# Profile view
@login_required(login_url='signin')
def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone')
        if CustomModel.objects.filter(email=email):
            messages.error(request, 'This email is already exit please try other email.')
        reg = CustomModel(first_name=first_name,last_name=last_name,email=email,phonenumber=phone_number)
        reg.set_password(password)
        reg.save()
        messages.success(request, 'Your profile saved successfully..')
        return redirect('home')
    return render(request, 'profile.html')

# Password Reset view
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('signin')