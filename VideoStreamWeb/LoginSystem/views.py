from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from LoginSystem.forms import *
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def SignUpUser(request):
    signup_form = UserCreationForm()
    registration = False
    same_name = False
    if request.method == 'POST':
        sign_form = UserCreationForm(data=request.POST)
        print("fsafadf")
        if sign_form.is_valid():
            print("fsafadsssf")
            sign_form.save()
            registration = True
        else :
            same_name=True
    dict = {'form' : signup_form,'Registered' : registration,'samename' : same_name}
    return render(request,'LoginSystem/SignUp.html',context=dict)

def LoginUser(request):
    Login_form = AuthenticationForm()
    if request.method == 'POST':
        Login_form = AuthenticationForm(data=request.POST)
        if Login_form.is_valid():
            username = Login_form.cleaned_data.get('username')
            password = Login_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

    return render(request,'LoginSystem/login.html',context={'form' : Login_form})
@login_required
def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def ProfileUser(request):
    return render(request,'LoginSystem/profile.html')

@login_required
def AddProfile(request):
    form = ProfileUploadForm()
    if request.method == 'POST':
        form = ProfileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save() 
            return HttpResponseRedirect(reverse('ProfileUser'))
    return render(request,'LoginSystem/change_profile.html',context={'form' : form})

def UpdateUser(request):
    form = ProfileUploadForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfileUploadForm(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('ProfileUser'))
    return render(request,'LoginSystem/change_profile.html',context={'form' : form})