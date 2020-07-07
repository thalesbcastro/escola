from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Serie(Base):
    TURMAS = (
        ('A', 'Turma A'),
        ('B', 'Turma B'),
        ('C', 'Turma C'),
    )
    ano = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    turma = models.CharField(max_length=5, choices=TURMAS)
    descricao = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'série'
        verbose_name_plural = 'séries'
        unique_together = ['ano', 'turma']

    def __str__(self):
        return f'{self.ano}º ano {self.turma} do Ensino Médio'


class Disciplinas(Base):
    DISC = (
        ('matematica', 'Matemática'),
        ('portugues', 'Português'),
        ('historia', 'História'),
        ('geografia', 'Geografia'),
        ('ingles', 'Inglês'),
        ('programacao', 'Programação'),
    )
    nome = models.CharField(max_length=20, choices=DISC)
    series = models.ManyToManyField(Serie)
    descricao = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'

    def __str__(self):
        return f'Disciplina de {self.nome}'


class Aluno(Base):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255, unique=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        return self.nome
