from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Aluno, Disciplinas, Serie
from .serializers import AlunosSerializer, DisciplinasSerializer, SerieSerializer


class DisciplinasAPIView(APIView):
    """
        API de Disciplinas da aplicação alunos
    """
    def get(self, request):
        disciplinas = Disciplinas.objects.all()  # Retornando todas as disciplinas
        serializer = DisciplinasSerializer(disciplinas, many=True)  # many=True porque são todas as disciplinas
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinasSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SeriesAPIView(APIView):
    """
        API das Séries da aplicação alunos do projeto django
    """
    def get(self, request):
        series = Serie.objects.all()  # query de todas as séries cadastradas
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)  # Retornando dados serializados

    def post(self, request):
        serializer = SerieSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlunosAPIView(APIView):
    """
        API do models Aluno da aplicação alunos do projeto Django
    """
    def get(self, request):
        alunos = Aluno.objects.all()  # Retorno de todos os alunos cadastrados
        serializer = AlunosSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunosSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
