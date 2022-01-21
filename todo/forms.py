from django.forms import ModelForm
from django.contrib.auth.models import User 
from .models import *

class addQuestionform(ModelForm):
    class Meta:
        model=Quizz
        fields = ['theme', 'question', 'op1', 'op2', 'op3', 'op4', 'ans']