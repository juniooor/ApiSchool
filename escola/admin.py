from django.contrib import admin
from escola.models import Aluno

# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome') #links que eu posso manipular
    search_fields = ('nome', ) #usado para buscar os alunos pelo nome



admin.site.register(Aluno, Alunos)