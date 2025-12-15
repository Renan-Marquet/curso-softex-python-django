from rest_framework import serializers
from .models import Tarefa
from django.utils import timezone

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
    class Meta:
        model = Tarefa
        """
        Serializer para Tarefa.
        Nota: O campo 'user' foi removido temporariamente.
        Na Apostila 4 será ingetado automaticamente pelo sevidor
        """
        #fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        fields = [
            'id', 
            'titulo', 
            'descricao', 
            'prioridade', 
            'prazo', 
            'concluida', 
            'data_conclusao', 
            'criada_em',
            ]
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ['id', 'criada_em', 'data_conclusao']
    
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
    
    
    def validate_prazo(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError(
            "O prazo não pode ser uma data no passado."
            )
        return value
    