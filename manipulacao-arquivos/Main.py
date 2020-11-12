#encoding='utf-8'
lista_compras = []
produto = ''

opcoes = ''' \nMenu
    1-  Parar
    2-	Adicionar produto na lista
    3-  Ver valores
Escolha: '''

def add_produto():
    produto = str(input('Informe o nome do produto: '))
    # lista_compras.append(produtos)
    arquivo = open("lista-compras.txt" , "a")
    arquivo.writelines(f'{produto} \n')
    arquivo.close()

def mostraValores():
    arquivo = open("lista-compras.txt", "r")
    print(arquivo.read())

while True:
    escolha = input(opcoes)
    if escolha == '1':
        break
    elif escolha == '2':
        print("\nAdicionar produto")
        add_produto()
    elif escolha == '3':
        print("\nMostra produtos \n --------")
        mostraValores()
    else:
        print('Valor digitado incorreto.')
