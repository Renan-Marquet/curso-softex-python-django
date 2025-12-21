#core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.exceptions import ValidationError 
from rest_framework import generics , status
from django.db import IntegrityError 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Tarefa
from .permissions import IsGerente
from .serializers import TarefaSerializer , UserRegistrationSerializer
import logging
logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    """
    View para listar todas as tarefas (GET).
    Endpoints:GET /api/tarefas/ - Lista todas as tarefas
    """
    def get(self, request, format=None):
        """
        Retorna lista de todas as tarefas do banco.
        Returns: Response: JSON com lista de tarefas e status 200
        """
        tarefas = Tarefa.objects.all()  # 1. BUSCAR: ORM do Django busca todos os registros
        serializer = TarefaSerializer(tarefas, many=True)  # 2. SERIALIZAR: Converter objetos Python → JSON  # many=True: indica que é uma lista de objetos   
        return Response(serializer.data, status=status.HTTP_200_OK) # 3. RESPONDER: Retornar JSON com status HTTP
    
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
        serializer = TarefaSerializer( data=request.data,context={'request': request} )  #Passa o request      
        if serializer.is_valid():# 2. VALIDAR: Checar se os dados são válidos
            serializer.save()  # 3. SALVAR: Persistir no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 4. RESPONDER: Retornar objeto criado + status 201
        # 5. ERRO: Retornar erros de validação + status 400
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    ''' 
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
    '''
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

    def get_object(self, pk): #"""Busca tarefa ou retorna 404.""" 
        return get_object_or_404(Tarefa, pk=pk) 
    def get(self, request, pk, format=None): 
        """ Retorna os dados de uma tarefa específica. 
        Args: 
            pk: ID da tarefa na URL 
        Returns: 
            200 OK: Tarefa encontrada 
            404 Not Found: Tarefa não existe """    
        tarefa = self.get_object(pk) # 1. BUSCAR: Usa método auxiliar (trata 404) 
        serializer = TarefaSerializer(tarefa) # 2. SERIALIZAR: Converte objeto único (sem many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)# 3. RESPONDER: Retorna JSON com status 200 
    
    def put(self, request, pk, format=None): 
        """ 
        Atualiza tarefa completamente (substituição total). 
        Exige que TODOS os campos editáveis sejam enviados. """ 
        tarefa = self.get_object(pk)  # 1. BUSCAR: Obter o objeto existente 
        serializer = TarefaSerializer(tarefa, data=request.data)  # 2. SERIALIZAR: Passar objeto antigo E novos dados
        if serializer.is_valid():  # 3. VALIDAR: Checar se JSON está completo e válido    
            serializer.save() # 4. SALVAR: Atualizar no banco
            return Response(serializer.data, status=status.HTTP_200_OK)  # 5. RESPONDER: Retornar objeto atualizado 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ERRO: Retornar erros de validação 
    
    def patch(self, request, pk, format=None): 
        """ 
        Atualiza tarefa parcialmente (merge). 
        Permite enviar apenas os campos que serão modificados. 
        """ 
       
        tarefa = self.get_object(pk)  # 1. BUSCAR: Obter o objeto existente 
        # 2. SERIALIZAR: Passar objeto, novos dados E partial=True 
        serializer = TarefaSerializer( 
            tarefa, 
            data=request.data, 
            partial=True # <--- ESSENCIAL PARA O PATCH 
            ) 
    
        if serializer.is_valid():     # 3. VALIDAR 
            serializer.save()  # 4. SALVAR (aplica apenas os campos recebidos) 
            return Response(serializer.data, status=status.HTTP_200_OK)  # 5. RESPONDER 
        else:    # ERRO 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): 
        """ 
        Remove um recurso específico. 
        """          
        tarefa = self.get_object(pk) # 1. BUSCAR: Obter o objeto (trata 404 se não existir)
        tarefa.delete()  # 2. DELETAR 
        return Response(status=status.HTTP_204_NO_CONTENT)  # # 3. RESPONDER: 204 No Content (sucesso sem corpo de resposta) 
    
class MinhaView(APIView): 
    permission_classes = [IsAuthenticated] # Adicionando a permissão 
    def get(self, request):  # Se chegou aqui, request.user é SEMPRE um objeto User logado     
        print(f"Usuário autenticado: {request.user.username}")

class TarefaListCreateAPIView(generics.ListCreateAPIView): 
    """ Lista tarefas e permite a criação de novas tarefas. PROTEGIDA: Requer autenticação JWT. """ 
    queryset = Tarefa.objects.all() 
    serializer_class = TarefaSerializer 
    permission_classes = [IsAuthenticated] # ← Proteção 
    # Exige Token válido 
    def get_queryset(self): 
        # """ Sobrescreve o comportamento padrão para retornar
        #  APENAS os dados pertencentes ao usuário logado. """ 
        user = self.request.user  # 1. Recupera o usuário validado pelo JWT 
        return Tarefa.objects.filter(user=user)  # 2. Retorna o filtro. O Django fará o WHERE user_id = X no banco.
    def perform_create(self, serializer): 
        # Garante que a tarefa criada seja vinculada ao usuário logado 
        serializer.save(user=self.request.user)
    # MÉTODO CHAVE: Injeta o usuário logado antes de salvar o objeto 
    def perform_create(self, serializer):
        """ 
        Associa a tarefa ao usuário logado (request.user) automaticamente. 
        """
         # request.user é garantido como autenticado pelo IsAuthenticated 
        serializer.save(user=self.request.user) 
        # A URL deve apontar para esta view em core/urls.py
        # path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefa-list-create'),

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    """ 
    Detalhes de tarefa, atualização e exclusão. 
    PROTEGIDA: Requer autenticação JWT. 
    """ 
    queryset = Tarefa.objects.all() 
    serializer_class = TarefaSerializer 
    def get_queryset(self): 
        return Tarefa.objects.filter(user=self.request.user) 
    def get_permissions(self): 
        """ Instancia e retorna a lista de permissões que esta view requer, 
        dependendo do método HTTP da requisição. """ 
        if self.request.method == 'DELETE': 
            # Para deletar: Precisa estar logado E ser Gerente 
            # # A ordem importa: primeiro checa login, depois o grupo 
            return [IsAuthenticated(), IsGerente()] 
        # Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset) 
        return [IsAuthenticated()]
    #permission_classes = [IsAuthenticated] # ← Proteção 
    # A URL deve apontar para esta view em core/urls.py 
    # path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefa-detail
class RegisterView(generics.CreateAPIView): 
    """ Endpoint para cadastro de novos usuários. 
    Acesso: Público (Qualquer um pode criar conta). """ 
    queryset = User.objects.all() 
    permission_classes = [AllowAny] # Sobrescreve o padrão global 
    serializer_class = UserRegistrationSerializer