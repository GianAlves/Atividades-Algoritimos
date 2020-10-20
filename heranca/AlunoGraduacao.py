from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f'Código: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}, Semestre: {self.semestre}')
