## Rodar projeto
**Obs.:** os endpoints estão no final do README

Caso desejem rodar o projeto localmente, é necessaŕio seguir os passos abaixo:
- Criar e ativar ambiente virtual, bem como instalar as dependências do projeto:

```commandline
python3.7 -m venv nome_do_seu_ambiente
```

```commandline
source nome_do_seu_ambiente/bin/activate
```

```commandline
pip install -r requirements.txt
```

Depois disso, faz-se necessário entrar na pasta do projeto (caso ainda não esteja) e executar (ao lado do arquivo _manage.py_) Para que as migrações sejam criadas:

```commandline
python manage.py migrate
```
Por fim, para rodar o servidor local, execute o seguinte comando:

```commandline
python manage.py runserver
```

## Explicação dos models do projeto (lógica)

Na aplicação criada, existem 3 modelos para a lógica do negócio:
- Serie
- Disciplinas
- Aluno

#### Série
Na tabela Serie existem os campos **ano**, **turma** e **descrição**, além de data de criação e modificação (prenchidos automaticamente), herdadas da classe base. Os campos **ano** e **turma** tornam a Série única (ex, 1º B) entre as demais (unique_together). Desses, apenas o campo descrição não é obrigatório. 
```python
    # ...
    ano = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    turma = models.CharField(max_length=5, choices=TURMAS)
    descricao = models.TextField(blank=True, default='')
```
#### Disciplinas

Já a tabela disciplina, tem os campos **nome**, **séries** e **descrição** (opcional), além dos herdados da Base (criação e modificação). O campo **séries** é um relacionamento Muitos para Muitos com a tabela anterior:
```python
    # ...
    nome = models.CharField(max_length=20, choices=DISC)
    series = models.ManyToManyField(Serie)
    descricao = models.TextField(blank=True, default='')
```  

#### Aluno

A tabela Aluno (classe Aluno) tem os campos **nome**, **matrícula** (unique) e **série**, além dos herdados do Base (classe Base). Um aluno tem um número único de matrícula e pertence apenas a uma série, sendo este campo, uma **FK** para a tabela Serie. Todos os campos são obrigatórios, desse modo, é preciso criar primeiro a **Série** com as **disciplinas** para poder criar o aluno:
```python
    # ...
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255, unique=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
``` 

### endpoints
- http://127.0.0.1:8000/api/v1/disciplinas/
- http://127.0.0.1:8000/api/v1/series/
- http://127.0.0.1:8000/api/v1/alunos/

 Para o método HTTP Get não é necessário nenhum tipo de autenticação. Para os outros, é necessário se autenticar via sessão (não por token). Ou seja, é necessário fazer login na API por meio da seguinte URL:
 
 - http://127.0.0.1:8000/auth/login/?next=/api/v1/
 
 Ou, simplesmente, ir no canto superior direito e clicar em **login**.
 O usuário é **admin** e a senha é **admin123**. Caso não consiga logar com essas credenciais, é necssário executar o seguinte comando com o ambiente virtual ativado e criar um superusuário:
 ```commandline
python manage.py createsuperuser
```
Para poder executar os demais métodos que são executados de forma individual, basta apenas colocar o **id** à frente de uma das URLs anteriores, por exemplo:
- http://127.0.0.1:8000/api/v1/alunos/1
