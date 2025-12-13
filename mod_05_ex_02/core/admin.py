from django.contrib import admin

from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'user', 'concluida','criada_em','prioridade', 'prazo']
    list_filter = ['concluida', 'criada_em']
    search_fields = ['prioridade','titulo', 'user__username']
    from .models import Tarefa

#Acerto