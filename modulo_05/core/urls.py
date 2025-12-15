from django.urls import path
from .views import ListaTarefasAPIView, DetalheTarefaAPIView
from .views import  TarefaListCreateAPIView, TarefaRetrieveUpdateDestroyAPIView
# LogoutView,
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
     path('tarefas/', 
          TarefaListCreateAPIView.as_view(), 
          name='tarefa-list-create'), 
     path('tarefas/<int:pk>/', 
          TarefaRetrieveUpdateDestroyAPIView.as_view(), 
          name='tarefa-detail'), 
     #path('logout/', LogoutView.as_view(), 
          #name='logout'), # ← Novo endpoint 
     ]