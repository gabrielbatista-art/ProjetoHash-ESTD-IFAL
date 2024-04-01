from pessoa import Pessoas
from buscaSequencial import buscaSequencial
import timeit

print("-------Busca Sequencial--------")
tamanhoLista = int(input("Digite o tamanho da lista: "))
listaSequencial = buscaSequencial()

print("Aguarde enquanto a lista é populada... \n")
start = timeit.default_timer()
for c in range(tamanhoLista - 1):
    listaSequencial.adicionarLista(Pessoas())
print(f"Lista populada. Tempo de execução para popular a lista com {tamanhoLista} de pessoas: {timeit.default_timer() - start :.2f}s \n")

while True:
    print("--------- MENU ---------\n [1]Adicionar na lista\n [2]Buscar CPF\n [3]Sair")
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        nome = input("Digite o nome: ")
        cpf = int(input("Digite o cpf: "))
        telefone = int(input("Digite o telefone: "))
        senha = int(input("Digite a senha: "))

        start = timeit.default_timer()
        listaSequencial.adicionarLista(Pessoas(nome=nome, cpf=cpf, telefone=telefone, senha=senha))
        print(f"{nome} adicionado. Tempo de execução{timeit.default_timer() - start :.2f}s")
    elif menu == 2:
        cpf = int(input("Digite o cpf: "))
        encontrou = False

        start = timeit.default_timer()
        for pessoa in listaSequencial.lista:
            if pessoa.cpf == cpf:
                print(f"nome: {pessoa.nome} \n telefone: {pessoa.telefone} \n cpf: {pessoa.cpf} \n senha: {pessoa.senha}")
                encontrou = True
        
        if encontrou == False:
            print("Pessoa não encontrada")
        
        print(f"Tempo de execução: {timeit.default_timer() - start :.2f}s")

