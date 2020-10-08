dadosAluno = {}

def calcularMedia(n1, n2):
    resultado = float((n1 + n2) / 2)
    dadosAluno['notaFinal'] = resultado

dadosAluno['nome'] = str(input('Digite seu nome: '))
dadosAluno['nota01'] = int(input('Digite sua nota01: '))
dadosAluno['nota02'] = int(input('Digite sua nota02: '))

calcularMedia(dadosAluno['nota01'], dadosAluno['nota02'])

# print('Nome: ' + dadosAluno['nome'] + ', Nota 01: ' + dadosAluno['nota01'] + ', Nota 02: ' + dadosAluno['nota02'] + ', Nota final: ' + dadosAluno['notaFinal'])

print(dadosAluno)