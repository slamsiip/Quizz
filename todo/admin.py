from django.contrib import admin
from .models import Quizz, Nourriture, Musique
# Register your models here.
	
admin.site.register(Quizz)
admin.site.register(Nourriture)
admin.site.register(Musique)