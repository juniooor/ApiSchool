from msilib.schema import Class
from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self):  
        #quando os alunos forem chamados vao ser chamandos em forma de string e nao de objeto como geralmente acontece
        return self.nome