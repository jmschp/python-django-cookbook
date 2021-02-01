from django.contrib import admin
from .models import Categoria, Receita 

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'data_categoria')


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'data_receita', 'categoria')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)