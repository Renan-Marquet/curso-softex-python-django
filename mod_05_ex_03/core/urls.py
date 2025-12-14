from django.urls import path
from .views import ListaTarefasAPIView, DetalheTarefaAPIView, ContagemTarefasAPIView
from . import views
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
     path('api/tarefas/contagem/', 
         ContagemTarefasAPIView.as_view()),
    path('tarefas/<int:tarefa_id>/duplicar/', 
         views.duplicar_tarefa, 
         name='duplicar_tarefa'),
]