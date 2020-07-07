from django.urls import path
from .views import DisciplinasAPIView, DisciplinaAPIView, SeriesAPIView, SerieAPIView, AlunosAPIView, AlunoAPIView

urlpatterns = [
    path('disciplinas/', DisciplinasAPIView.as_view(), name='disciplinas'),
    path('disciplinas/<int:pk>/', DisciplinaAPIView.as_view(), name='disciplina'),
    path('series/', SeriesAPIView.as_view(), name='series'),
    path('series/<int:pk>/', SerieAPIView.as_view(), name='serie'),
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('alunos/<int:pk>/', AlunoAPIView.as_view(), name='aluno'),
]