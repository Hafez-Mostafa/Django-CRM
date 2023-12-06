from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials. Please try again.')



    return render(request,'home.html',{})

# def login_user(request):
#     return render(request,'login.html',{})
def logout_user(request):

    # Log the user out
    logout(request)
    
    # Add a success message
    messages.success(request, 'Logged out Successfully')
    
    # Redirect the user to the 'home' page
    return redirect('home')



def register_user(request):
    return render(request,'register.html',{})