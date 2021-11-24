from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import CreateUserForm


# Register User Page
def registerPage(request):
    # authenticated users are not allowed on this page
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        # user registration page
        form = CreateUserForm()  # custom userform

        if request.method == 'POST':
            form = CreateUserForm(request.POST or None)
            if form.is_valid():
                new = form.save(commit=False)
                new.save()
                user = form.cleaned_data.get("username")
                messages.success(request,
                                 user.upper() + ', account created!,\
                                     confirm your email inbox for the account \
                                         activation Link.')
                # send new user to login page
                # TO DO: send a verificatio email
                return redirect('register')

    context = {'form': form}

    return render(request,
                  'accounts/register.html', context)


# Login Page
def loginPage(request):

    # check if user is authenticated and send them to dashboard
    if request.user.is_authenticated:
        return redirect('profile')

    else:
        if request.method == 'POST':
            # get user email and password
            email = request.POST.get("email")
            password = request.POST.get("password")

            # authenticate the email and password
            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                # profile has not been updated redirect to profile update page
                # if user account is free redirect to inventory
                # else redirect to dashboard
                return redirect('dashboard')
            else:
                messages.error(request,
                               'Username or password is incorrect!')

    return render(request, 'accounts/login.html')


# Logout Url
def logoutUrl(request):
    # logout user
    logout(request)
    return redirect('login')


# forgot Password
def forgortPassword(request):
    return render(request, 'accounts/forgot.html')


# Reset Password
def resetPassword(request):
    return render(request, 'accounts/reset.html')
