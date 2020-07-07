from rest_framework import generics
from .models import Disciplinas, Serie, Aluno
from .serializers import DisciplinasSerializer, SerieSerializer, AlunosSerializer


class DisciplinasAPIView(generics.ListCreateAPIView):  # ListCreateAPIView = Lista e cria sem precisar de ID
    """
        API de Disciplinas da aplicação alunos
    """
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer


class DisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):  # Lista, Update e Delete pelo ID
    """
        API de Disciplinas da aplicação alunos
    """
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer


class SeriesAPIView(generics.ListCreateAPIView):
    """
        API das Séries da aplicação alunos do projeto django
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class SerieAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API das Séries da aplicação alunos do projeto django
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class AlunosAPIView(generics.ListCreateAPIView):
    """
        API do models Aluno da aplicação alunos do projeto Django
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer


class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API do models Aluno da aplicação alunos do projeto Django
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
