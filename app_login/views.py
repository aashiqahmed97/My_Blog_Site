from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login ,authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import signUpForm , UserProfileChange , profilePic



def sign_up(request):
    form = signUpForm()
    registered = False
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True

    context={'form':form, 'registered':registered}  
    return render(request,'app_login/signup.html',context)    


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully")
                return redirect('app_blog:blog_list')
            else:
                print("Authentication failed")
        else:
            print("Form is invalid")

    return render(request, 'app_login/login.html', context={'form': form})
           
@login_required
def log_out(request):
    logout(request)
    messages.info(request,'user is logout')
    return redirect('app_login:login')
                
@login_required
def profile(request):
    context = {}
    return render ( request, 'app_login/profile.html', context)
@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST , instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)

    return render (request, 'app_login/changeProfile.html', context = {'form': form})        


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(instance=current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()

            changed = True
    return render(request , 'app_login/change_pass.html' , context = {'form':form , 'changed':changed})        
@login_required
def add_pro_pic(request):
    
    form = profilePic()
    if request.method == 'POST':
        form = profilePic(request.POST , request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return redirect ('app_login:profile')
    return render (request , 'app_login/pro_pic_add.html', context={'form':form})
@login_required
def change_pro_pic(request):
    form = profilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = profilePic(request.POST , request.FILES , instance =request.user.user_profile)
        if form.is_valid(): 
            form.save()
            return redirect ('app_login:profile')

    return render (request , 'app_login/pro_pic_add.html', context={'form':form})  