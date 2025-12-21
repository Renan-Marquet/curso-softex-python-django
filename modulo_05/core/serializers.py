from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth.models import User, Group

class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o Model Tarefa.
    Responsabilidades:
    1. Converter Tarefa → JSON (serialização)
    2. Converter JSON → Tarefa (desserialização)
    3. Validar dados de entrada
    """
    # Customizar mensagens padrão
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
        }
        )

    """ 
    Serializer para Tarefa com segurança.
      O campo 'user' é exibido (read-only) mas NÃO aceito na entrada. 
    """
        # 1. Mostra o username do usuário em vez do ID (read-only na saída) 
    user = serializers.StringRelatedField(read_only=True)
    


    class Meta:
        model = Tarefa
        """
        Serializer para Tarefa.
        Nota: O campo 'user' foi removido temporariamente.
        Na Apostila 4 será ingetado automaticamente pelo sevidor
        """
        #fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        fields = ['id','user', 'titulo', 'concluida', 'criada_em']
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ['id','user', 'criada_em']
    
    def validate_titulo(self, value):
        """
        Validação customizada para o campo 'titulo'.
        Regras:
        - Não pode ser vazio (após strip)
        - Não pode conter apenas números
        - Deve ter pelo menos 3 caracteres
        """
        # Remover espaços em branco
        value = value.strip()
        # Validação 1: Não vazio
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )
        # Validação 2: Mínimo de caracteres
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )
        # Validação 3: Não apenas números
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )
        return value
    """
    #def validate_titulo(self, value):
        #Impedir títulos duplicados para o mesmo usuário.
        user = self.context['request'].user
        if Tarefa.objects.filter(user=user, titulo=value).exists():
            raise serializers.ValidationError(
                "Você já tem uma tarefa com este título."
            )
        return value
    """
    
    def validate(self, data):
        """
        Validação de objeto completo (múltiplos campos).
        Exemplo: Tarefas com palavra "urgente" não podem
        começar como concluídas.
        """
        titulo = data.get('titulo', '').lower()
        concluida = data.get('concluida', False)

        if 'urgente' in titulo and concluida:
            raise serializers.ValidationError(
                "Tarefas urgentes não podem ser criadas como concluídas."
            )
        return data
    
class UserRegistrationSerializer(serializers.ModelSerializer): 
    # Definimos 'write_only=True' para que a senha seja aceita no cadastro (POST), 
    # # mas NUNCA seja devolvida na resposta (Response JSON). 
    password = serializers.CharField( 
        write_only=True, 
        required=True, 
        style={'input_type': 'password'} ) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password'] 
    def create(self, validated_data): 
        """ Intercepta a criação para usar o 'create_user' e hashear a senha. """ 
        # Extrai a senha dos dados validados 
        password = validated_data.pop('password') 
        # Extrai email e username 
        email = validated_data.get('email', '') 
        username = validated_data['username'] 
        # Cria a instância usando o método seguro do Django 
        user = User.objects.create_user( 
            username=validated_data['username'], 
            email=validated_data.get('email', ''), 
            password=password 
        ) 
        # 2. Lógica de Atribuição de Cargo (Role) 
        try: 
            # Busca o grupo 'Comum' 
            grupo_comum = Group.objects.get(name='Comum') 
            # Adiciona o usuário ao grupo 
            user.groups.add(grupo_comum) 
        except Group.DoesNotExist: 
            # Fallback: Se o grupo não existir, o usuário é criado sem grupo. 
            # # Em produção, deveríamos logar um erro aqui. 
            pass
        return user