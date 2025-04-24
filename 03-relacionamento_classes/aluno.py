
class Disciplina:
    def __init__(self,nome,carga_horaria):
        self.__nome = nome
        self.__carga_horaria = carga_horaria
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo

    @property 
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        self.__carga_horaria = nova_carga_horaria

    def __str__(self):
        return f'{self.__nome} ({self.__carga_horaria})'
        

class Aluno:
    def __init__(self,nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina

    def __str__(self):
        return f'\nAluno - {self.__nome}\nDisciplina - ({self.__disciplina})\n'

# relacionamento 

aluno1 = Aluno('João', Disciplina('Estrutura de Dados', 67))
aluno2 = Aluno('Maria', Disciplina('Banco de dados I',87))

print('Aluno 1:', aluno1)

print('Aluno 2:', aluno2)     