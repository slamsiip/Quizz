from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Quizz, Nourriture, Musique


def currenttodos(request):
    if request.method == 'POST':
        print(request.POST)
        quizzs=Quizz.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in quizzs:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, 'todo/currenttodos.html', {'quizzs':quizzs})
    else:
        quizzs=Quizz.objects.all()
        context = {
            'questions':quizzs
        }
        return render(request, 'todo/currenttodos.html', {'quizzs':quizzs})

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

def animals(request):
	quizzs = Quizz.objects.all()
	return render(request, 'todo/animals.html',{'quizzs':quizzs} )	

def musique(request):
	quizzs = Musique.objects.all()
	return render(request, 'todo/musique.html',{'quizzs':quizzs} )	

def nourriture(request):
	quizzs = Nourriture.objects.all()
	return render(request, 'todo/nourriture.html',{'quizzs':quizzs} )	

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
				return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already be taken, please choose a new one '})
		else : 
			return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})