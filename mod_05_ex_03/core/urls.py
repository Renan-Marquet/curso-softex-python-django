from django.urls import path
from .views import (ListaTarefasAPIView, DetalheTarefaAPIView, ContagemTarefasAPIView, duplicar_tarefa,)
# from . import views
# Namespace do app (útil para reverse())
app_name = 'core'
urlpatterns = [
    # /api/tarefas/ → ListaTarefasAPIView
    # COLEÇÃO: /api/tarefas/
    path('tarefas/', 
        ListaTarefasAPIView.as_view(), 
        name='lista-tarefas'),
         # RECURSO INDIVIDUAL: /api/tarefas/<pk>/ 
    path('tarefas/<int:pk>/', 
        DetalheTarefaAPIView.as_view(), 
        name='detalhe-tarefa'),
    path('tarefas/contagem/', 
        ContagemTarefasAPIView.as_view(),
        name='contagem-tarefas'),
    path('tarefas/<int:pk>/duplicar/', 
        duplicar_tarefa, 
        name='duplicar_tarefa'),
]