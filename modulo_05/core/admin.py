from django.contrib import admin
from rest_framework.authtoken.models import Token

# Register your models here.
from .models import Tarefa

admin.site.register(Token)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'user', 'concluida', 'criada_em']
    list_filter = ['concluida', 'criada_em']
    search_fields = ['titulo', 'user__username']