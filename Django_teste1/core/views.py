from django.shortcuts import render
#from django.http import HttpResponse
from .models import Tarefa

def home(request):
    # 2. Use o ORM para buscar os dados! 
    # # Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa" 
    todas_as_tarefas = Tarefa.objects.all() 

    context = {
        'nome_usuario':'Renan',
        'tecnologias':['Python','Django','HTML','CSS','Models','Admin'],
        'tarefas': todas_as_tarefas # 4. Adicione as tarefas ao contexto
    }



    return render(request, 'home.html', context)
    #return HttpResponse("<h1>Olá Mundo! Esta é a minha terceira página Django!<h1>")

# Create your views here.
