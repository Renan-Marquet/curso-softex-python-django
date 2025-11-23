from django.urls import path
from . import views

urlpatterns =[
    # Nossas URLS antigas
    path('',views.home, name='home'),

    # NOSSAS NOVAS URLs DINÂMICAS 
    # # Ex: /tarefa/5/concluir/ 
    # # <int:pk> captura um inteiro da URL e o passa para a view como um argumento chamado 'pk' 
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),

    # Ex: /tarefa/5/deletar/ 
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'), 

    # ADICIONE A URL DE CADASTRO 
    path('register/', views.register, name='register'),
    ]
