from django.contrib import admin
from .models import Quizz, Nourriture, Musique, Scored
# Register your models here.
	
admin.site.register(Quizz)
admin.site.register(Nourriture)
admin.site.register(Musique)
admin.site.register(Scored)