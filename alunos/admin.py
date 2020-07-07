from django.contrib import admin
from .models import Aluno, Serie, Disciplinas


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('ano', 'turma', 'descricao', 'criacao', 'modificacao')


@admin.register(Disciplinas)
class DisciplinasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'modificacao')
    list_filter = ['series']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'serie', 'criacao', 'modificacao')
    list_filter = ['serie']
