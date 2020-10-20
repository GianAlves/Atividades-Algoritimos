class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f'Código: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}')
