from buscaBinaria import BuscaBinaria
from pessoa import Pessoas
import timeit


print("------BUSCA BINÁRIA------")
tamanhoLista = int(input("Digite o tamanho da lista: "))
buscaBin = BuscaBinaria()

print("Populando lista...")
start = timeit.default_timer()
for c in range(tamanhoLista):
    buscaBin.add(Pessoas())
print(f"Lista populada por {tamanhoLista} entidades.\nTempo de execução: {timeit.default_timer() - start :.2f}s")

while True:
    print("[1] Adicionar pessoa\n[2] Buscar cpf\n[3] Sair")
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        nome = input("Digite o nome: ")
        cpf = int(input("Digite o cpf: "))
        telefone = int(input("Digite o telefone: "))
        senha = int(input("Digite a senha: "))

        start = timeit.default_timer()
        buscaBin.add(Pessoas(nome=nome, cpf=cpf, telefone=telefone, senha=senha))
        print(f"{nome} Adicionado em {timeit.default_timer() - start :.2f}s")
    elif menu == 2:
        cpf = int(input("Digite o cpf: "))

        start = timeit.default_timer()
        pessoa = buscaBin.busca_bi(cpf)
        print(f"A pessoa é: {pessoa.nome}\n Seu cpf é: {pessoa.cpf}\n Seu telefone: {pessoa.telefone}\n Sua senha: {pessoa.senha}")
        print(f"Tempo de execução: {timeit.default_timer() - start :.2f}s")
    elif menu == 3:
        break

