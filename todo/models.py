from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quizz(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class Musique(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class Nourriture(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,blank=True)
    op2 = models.CharField(max_length=200,blank=True)
    op3 = models.CharField(max_length=200,blank=True)
    op4 = models.CharField(max_length=200,blank=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question        

class Score(models.Model):
    score = models.TextField()
    def __str__(self):
        return self.score  
        
class Scored(models.Model):
    score = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.score          