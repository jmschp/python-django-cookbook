from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    data_categoria = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoria
    

class Receita(models.Model):
    nome_receita = models.CharField(max_length=50, unique=True)
    ingredientes = models.TextField(max_length=500)
    modo_preparo = models.TextField(max_length=2000)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=50)
    data_receita = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
