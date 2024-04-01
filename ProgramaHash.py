from pessoa import Pessoas
from hashClasse import HashPessoas
import timeit

print("-------Busca Hash--------")
tamanhoLista = int(input("Digite o tamanho da lista: "))
buscaHash = HashPessoas(tamanhoLista)
print("Aguarde enquanto a lista é populada...")
start = timeit.default_timer()
listaPessoas = [Pessoas() for c in range(tamanhoLista - 3)]
for pessoa in listaPessoas:
    buscaHash.adicionarLista(pessoa)
print(f"Lista populada. Tempo de exeução para adicionar {tamanhoLista} pessoas: {timeit.default_timer() - start :.2f}s")


while True:
    print("[1] Adicionar Pessoa\n [2]Buscar Por Cpf\n [3]Sair")
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        nome = input("Digite o nome: ")
        cpf = int(input("Digite o cpf: "))
        telefone = int(input("Digite o telefone: "))
        senha = int(input("Digite a senha: "))

        start = timeit.default_timer()
        buscaHash.adicionarLista(Pessoas(nome=nome, cpf=cpf, telefone=telefone, senha=senha))
        print(f"{nome} Adicionado em {timeit.default_timer() - start :.2f}s")
    elif menu == 2:
        cpf = int(input("Digite o numero do cpf: "))
        start = timeit.default_timer()
        pessoa = buscaHash.procurarCpf(cpf)
        print(f"A pessoa é: {pessoa.nome}\n Seu cpf é: {pessoa.cpf}\n Seu telefone: {pessoa.telefone}\n Sua senha: {pessoa.senha}")
        print(f"Tempo de execução: {timeit.default_timer() - start :.2f}s")
    elif menu == 3:
        break
