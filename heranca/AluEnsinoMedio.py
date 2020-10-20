from Aluno import Aluno


class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f'Código: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}, Ano: {self.ano}')
