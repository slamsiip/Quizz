from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import *
from django.contrib.auth import login, logout, authenticate
from .models import Quizz, Scored

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
		else: 
			login(request, user)
			return redirect('home')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

def home(request):
	#quizzs = Quizz.objects.all()
#	next = request.POST.get('next', '/')
	if request.method == 'POST':	
		request.session['test'] = request.POST.get("next")	
		request.session.get('test')
		return redirect('animaux')	
	return render(request, 'todo/home.html', {'quizzs': ["animaux", "musique", "autres"]})	

def animaux(request):
    var = request.session['test']
    if request.method == 'POST':
        theme = var
        quizzs=Quizz.objects.all()
        scor=0
        total = 0 
        for q in quizzs:
            if q.theme == var:
                total += 1
                if q.ans ==  request.POST.get(q.question):
                    scor += 1
        if total != 0:            
        	percent = int((scor/total)*100)
        else :
        	return render(request, 'todo/animaux.html',{'quizzs':quizzs, 'var':var, 'error':'Pas de question dans ce questionnaire, on en créer ?'})	
        context = {
        	'theme':theme,
            'score':scor,
            'time': request.POST.get('timer'),
            'percent':percent,
            'var' : var,
        }
        Scored.objects.create(user=request.user, score=percent, theme = theme).save()
        return render(request, 'todo/currenttodos.html',context)
    else:
        quizzs=Quizz.objects.all()
        total = 0 
        for q in quizzs:
            if q.theme == var:
                total += 1
        return render(request, 'todo/animaux.html',{'quizzs':quizzs,'total':total,  'var':var})

def musique(request):   
    form=addQuestionform()
    if(request.method=='POST'):
        form=addQuestionform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'todo/musique.html',context)


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
				return redirect('home')
			except IntegrityError:
				return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already be taken, please choose a new one '})
		else : 
			return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def history(request):
	quizzs = Quizz.objects.all()	
	profiles = Scored.objects.filter(user=request.user)

	score_total_an = 0
	count_an = 0 
	score_total_m = 0
	count_m = 0 
	score_total_a = 0
	count_a = 0 

	for p in profiles : 
		if p.theme == "animaux":
			score_total_an += int(p.score)
			count_an += 1 
		elif p.theme == "musique":
			score_total_m += int(p.score)
			count_m += 1 
			print(p.score)
		elif p.theme == "autres":
			score_total_a += int(p.score)
			count_a += 1 

	if count_a != 0 : 		
		score_total_autre = str(round(score_total_a/count_a, 1)) + "%" 
	else: 
		score_total_autre = " Pas encore de score pour le quizz autre"		

	if count_m != 0:
		score_total_musique = str(round(score_total_m/count_m, 1)) + "%"
	else :
		score_total_musique = " Pas encore de score pour le quizz musique"	

	if count_an != 0:
		score_total_animaux= str(round(score_total_an/count_an, 1)) + "%"	
	else: 
		score_total_animaux= " Pas encore de score pour le quizz animaux"		
		print(score_total_m, count_m)
	context = {
        	'score_total_musique':score_total_musique,
            'score_total_animaux':score_total_animaux,
            'score_total_autre': score_total_autre,
            'count_a':count_a,
            'count_an':count_an,
            'count_m':count_m,
        }
	return render(request, 'todo/history.html', context)
