from django.urls import path
from .views import ListaTarefasAPIView, DetalheTarefaAPIView
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
]