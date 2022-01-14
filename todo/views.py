from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Quizz


def currenttodos(request):
	return render(request, 'todo/currenttodos.html')	

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
		else: 
			login(request, user)
			return redirect('currenttodos')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

def home(request):
	quizzs = Quizz.objects.all()
	return render(request, 'todo/home.html', {'quizzs':quizzs})	


def signupuser(request):
	if request.method == 'GET':
		return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=(request.POST['password1']))
				user.save()
				login(request, user)
				return redirect('currenttodos')
			except IntegrityError:
				return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already be taken, pls choose a new one '})
		else : 
			return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})