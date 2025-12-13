#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError 
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    """
    View para listar todas as tarefas (GET).
    Endpoints:
    GET /api/tarefas/ - Lista todas as tarefas
    """
    def get(self, request, format=None):
        """
        Retorna lista de todas as tarefas do banco.
        Returns:
        Response: JSON com lista de tarefas e status 200
        """
        # 1. BUSCAR: ORM do Django busca todos os registros
        tarefas = Tarefa.objects.all()

        # 2. SERIALIZAR: Converter objetos Python → JSON
        # many=True: indica que é uma lista de objetos

        serializer = TarefaSerializer(tarefas, many=True)

        
        
        # 3. RESPONDER: Retornar JSON com status HTTP
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
            )
    
    def post(self, request, format=None):
        """
        Cria uma nova tarefa.
        Args:
            request.data: JSON com dados da tarefa
            {
            "titulo": "string",
            "concluida": boolean (opcional, default=False)
            }
        Returns:
            201 Created: Tarefa criada com sucesso
            400 Bad Request: Dados inválidos
        """
        
        # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(
            data=request.data,
            context={'request': request} #Passa o request
            )
        # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
            # 3. SALVAR: Persistir no banco de dados
            serializer.save()
            # 4. RESPONDER: Retornar objeto criado + status 201
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        # 5. ERRO: Retornar erros de validação + status 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        """
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED
                    )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            # Erro de constraint no banco (ex: UNIQUE)
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Erro inesperado
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        """
    """     
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Tarefa criada: {serializer.data['id']}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            """
class DetalheTarefaAPIView(APIView): 
    """
    def get(self, request, pk, format=None): 
        # ^^ 
        # # Parâmetro capturado da URL 
        print(f"Buscando tarefa com ID: {pk}")
        try:
           tarefa = Tarefa.objects.get(pk=pk) 
        except Tarefa.DoesNotExist: return Response({'error': 'Tarefa não encontrada'}, status=404)
    """
        #tarefa = get_object_or_404(Tarefa, pk=pk) 
        # Automaticamente lança uma exceção Http404 se não encontrar
    #""" View para operações em recurso individual. """ 
    #def get_object(self, pk): 
        #""" Busca a tarefa pelo ID e retorna 404 se não encontrada. """ 
        #return get_object_or_404(Tarefa, pk=pk) 
    # ... Métodos GET, PUT, PATCH, DELETE usarão self.get_object(pk)

    def get_object(self, pk): 
        """Busca tarefa ou retorna 404.""" 
        return get_object_or_404(Tarefa, pk=pk) 
    def get(self, request, pk, format=None): 
        """ Retorna os dados de uma tarefa específica. 
        Args: 
            pk: ID da tarefa na URL 
        Returns: 
            200 OK: Tarefa encontrada 
            404 Not Found: Tarefa não existe """
        # 1. BUSCAR: Usa método auxiliar (trata 404) 
        tarefa = self.get_object(pk) 
        # 2. SERIALIZAR: Converte objeto único (sem many=True) 
        serializer = TarefaSerializer(tarefa) 
        # 3. RESPONDER: Retorna JSON com status 200 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None): 
        """ 
        Atualiza tarefa completamente (substituição total). 
        Exige que TODOS os campos editáveis sejam enviados. """ 
        # 1. BUSCAR: Obter o objeto existente 
        tarefa = self.get_object(pk) 
        # 2. SERIALIZAR: Passar objeto antigo E novos dados 
        serializer = TarefaSerializer(tarefa, data=request.data) 
        # ^^^^^ ^^^^^^^^^^^^^^^^ 
        # # | Nova versão 
        # # Versão atual 
        # # 3. VALIDAR: Checar se JSON está completo e válido 
        if serializer.is_valid(): 
            # 4. SALVAR: Atualizar no banco 
            serializer.save() 
            # 5. RESPONDER: Retornar objeto atualizado 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        # ERRO: Retornar erros de validação 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None): 
        """ 
        Atualiza tarefa parcialmente (merge). 
        Permite enviar apenas os campos que serão modificados. 
        """ 
        # 1. BUSCAR: Obter o objeto existente 
        tarefa = self.get_object(pk) 
        # 2. SERIALIZAR: Passar objeto, novos dados E partial=True 
        serializer = TarefaSerializer( 
            tarefa, 
            data=request.data, 
            partial=True # <--- ESSENCIAL PARA O PATCH 
            ) 
        # 3. VALIDAR 
        if serializer.is_valid(): 
            # 4. SALVAR (aplica apenas os campos recebidos) 
            serializer.save() 
            # 5. RESPONDER 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        # ERRO 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): 
        """ 
        Remove um recurso específico. 
        """ 
        # 1. BUSCAR: Obter o objeto (trata 404 se não existir) 
        tarefa = self.get_object(pk) 
        # 2. DELETAR 
        tarefa.delete() 
        # # 3. RESPONDER: 204 No Content (sucesso sem corpo de resposta) 
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()

        return Response({
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes
        }, status=status.HTTP_200_OK)