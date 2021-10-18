base = []
usuarios = {}
def perguntar():
    return int(input("O que deseja realizar? \n"+
                     "1 - para inserir um usuário \n"+
                     "2 - para pesquisar um usuário \n"+
                     "3 - para excluir um usuário \n"+
                     "4 - para listar os usuários \n"))

def inserir():
    login = str(input("Digite o login único: "))
    nome = str(input("Digite o nome: "))
    profissao = str(input("Digite a profissão: "))
    salario = float(input("Digite o salário: "))
    usuarios[login] = [nome, profissao, salario]

    with open("bd.txt", "a") as arquivo:
            arquivo.write(login+",{},{},{}\n".format(nome, profissao, salario))

def pegar():
    with open("bd.txt", "r") as arquivo:
     for registro in arquivo.readlines():
        base.append(registro.replace("\n", "")
                    .replace("['", "")
                    .replace("']", "")
                    .split(","))
        for c in range(len(base)):
            usuarios[base[c][0]] = [base[c][1], base[c][2], base[c][3]]

def pesquisar(login):
    pegar()
    print(usuarios.get(login))


def exibir():
    pegar()
    print(usuarios)


def excluir(login):
    pegar()
    usuarios.pop(login)
    with open("bd.txt", 'w') as arquivo:
        pass
    for chave, valor in usuarios.items():
        with open("bd.txt", 'a') as arquivo:

            arquivo.write(str(chave)+",{},{},{}\n".format(str(usuarios[chave][0]),
                                                           str(usuarios[chave][1]),
                                                           str(usuarios[chave][2])))
    base.clear()
