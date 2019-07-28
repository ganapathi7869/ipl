from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from iplapp.form.auth import *
from django.contrib.auth import authenticate,login,logout

class LoginView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/iplapp/seasons/')
        form = LoginForm()
        return render(
            request,
            template_name='login.html',
            context={
                'form': form,
            }
        )

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request,user)
                return redirect('/iplapp/seasons/')
            else:
                messages.error(request,'Invalid user credentials')
        return render(
            request,
            template_name="login.html",
            context={
                'form':form,
            }
        )

class SignupView(View):
    def get(self,request):
        form = SignUpForm()
        return render(
            request,
            template_name='signup.html',
            context={
                'form': form,
            }
        )

    def post(self,request,*args,**kwargs):
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            user.save()
            form.save()
            if user is not None:
                return redirect('/iplapp/login/')
            else:
                messages.error(request,'Invalid user credentials')

        else:
            return render(
                request,
                template_name='signup.html',
                context={
                    'form': form,
                }
            )

def logout_user(request):
    logout(request)
    return redirect('/iplapp/seasons/')
