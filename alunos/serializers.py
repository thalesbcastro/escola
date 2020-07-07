from rest_framework import serializers
from .models import Disciplinas, Serie, Aluno


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'ano', 'turma', 'descricao', 'disciplinas')


class DisciplinasSerializer(serializers.ModelSerializer):
    # Nested Relationship
    class Meta:
        model = Disciplinas
        fields = ('id', 'nome', 'series', 'descricao', 'criacao', 'modificacao')


class AlunosSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # serie = SerieSerializer(read_only=True)

    class Meta:
        extra_kwargs = {
            # Informação pessoal
            'matricula': {'write_only': True}
        }
        model = Aluno
        fields = ('id', 'nome', 'matricula', 'serie')
