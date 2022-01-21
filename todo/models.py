from django.db import models
from django.contrib.auth.models import User

# Create your models here.



        
class Scored(models.Model):
    choix = (("animaux", "animaux"), ("musique","musique"),("autres","autres"))
    theme = models.CharField(max_length=100, choices = choix)
    score = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.score          

class Quizz(models.Model):
    choix = (("animaux", "animaux"), ("musique","musique"),("autres","autres"))
    theme = models.CharField(max_length=100, choices = choix)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
 

    def __str__(self):
        return self.theme        