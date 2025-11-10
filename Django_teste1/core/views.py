from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    context = {
        'nome_usuario':'Renan',
        'tecnologias':['Python','Django','HTML','CSS']
    }




    return render(request, 'home.html',context)
    #return HttpResponse("<h1>Olá Mundo! Esta é a minha terceira página Django!<h1>")

# Create your views here.
