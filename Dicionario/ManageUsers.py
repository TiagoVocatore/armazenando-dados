from Dicionario.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        inserir()
    if opcao == 2:
        pesquisar(str(input("Digite o login único do usuário a ser pesquisado: ")))
    if opcao == 3:
        excluir(str(input("Digite o login único do usuário a ser excluído: ")))
    if opcao == 4:
        exibir()
    opcao = perguntar()



