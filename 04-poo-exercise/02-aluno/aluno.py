class Aluno:
    def __init__(self,matricula:int,nome:str,notas:list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self) -> str: 
        return f'Matrícula: {self.__matricula}'
    
    
    def media(self):
        return f'{sum(self.__notas)/ len(self.__notas):.2f}'
    
    def adiciona_nota(self,nota):
        self.__notas.append(nota)
    
    def __str__(self):
        return f'Nome do aluno: {self.__nome}, Matrícula: {self.__matricula}\nNotas: {"       ".join(map(str, self.__notas))}\nMedia: {self.media()}\n'
    
# aluno1 = Aluno(123, "João", [8.0, 7.5, 9.0])
# print(aluno1)
# print(aluno1.media())
from random import randint
def criar_alunos(quantidade):
    lista_de_alunos = []
    for i in range(quantidade):
        aluno = Aluno(
            randint(1000, 9999),
            f'Aluno {i+1}',
            [randint(0, 10), randint(0, 10), randint(0, 10)]
        )
        lista_de_alunos.append(aluno)
    return lista_de_alunos

lista_de_alunos = criar_alunos(5)
for aluno in lista_de_alunos:
    print(aluno)

