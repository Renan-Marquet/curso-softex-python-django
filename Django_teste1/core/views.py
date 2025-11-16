# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm

def home(request):
    # 2. Use o ORM para buscar os dados! 
    # 3. Lógica de POST: Se o formulário foi enviado 
    if request.method == 'POST': 
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST) 
        # 4. O Django valida os dados (max_length, etc.) 
        if form.is_valid(): 
            # 5. Salva o objeto no banco de dados! 
            form.save() 
            # 6. Redireciona de volta para a 'home' 
            # # Isso é o Padrão "Post-Redirect-Get" (PRG) 
            return redirect('home') 
        # Se o form NÃO for válido, o código continua e
        # o 'form' (com os erros) será enviado para o template
     # 7. Lógica de GET: Se o usuário apenas visitou a página
    else: 
        form = TarefaForm() 
        # Cria um formulário vazio
    # # Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa" 
    todas_as_tarefas = Tarefa.objects.all() 

    context = {
        'nome_usuario':'Renan',
        'tecnologias':['Python','Django','HTML','CSS','Models','Admin'],
        'tarefas': todas_as_tarefas,# 4. Adicione as tarefas ao contexto
        'form':form
    }
    return render(request, 'home.html', context)
    #return HttpResponse("<h1>Olá Mundo! Esta é a minha terceira página Django!<h1>")

def concluir_tarefa(request, pk):
     # 1. Busca a tarefa pela 'pk' (ID) vinda da URL.
     #  # Se não achar, retorna um erro 404. 
    tarefa = get_object_or_404(Tarefa, pk=pk) 
    
    # 2. Segurança: Apenas execute se o método for POST 
    if request.method == 'POST': 
        # 3. A Lógica de "Update" 
        tarefa.concluida = True 
        tarefa.save() # Não se esqueça de salvar! 
        
        # 4. Redireciona de volta para a 'home' (Padrão PRG) 
        return redirect('home') 
    
   
def deletar_tarefa(request, pk): 
    # 1. Busca a tarefa 
    tarefa = get_object_or_404(Tarefa, pk=pk) 
    # 2. Segurança: Apenas execute se o método for POST 
    if request.method == 'POST': 
        # 3. A Lógica de "Delete" 
        tarefa.delete() 

        # 4. Redireciona de volta para a 'home' 
        return redirect('home')



