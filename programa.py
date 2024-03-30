import random
from pessoa import Pessoas
from hashClasse import HashPessoas
from buscaSequencial import buscaSequencial

ListaPessoasSequencial = buscaSequencial()
ListaPessoasHash = HashPessoas(10003)
listaPessoas = []

pessoa1 = Pessoas(10345678911, 'nome', 123456789, 3456789)
pessoa2 = Pessoas(10345678912, 'noma', 123456789, 3456789)
pessoa3 = Pessoas(10345678913, 'nomo', 123456789, 3456789)

# for c in range(10000):
#     listaPessoas.append(Pessoas(random.randrange(11111111112, 99999999998), 'nome', 123456789, 346890))

for c in range(1000000):
    pass #Busca sequencial

for pessoa in listaPessoas:
    ListaPessoasHash.adicionarLista(pessoa)
    print("Adicionou pessoa")

ListaPessoasHash.adicionarLista(pessoa1)
ListaPessoasHash.adicionarLista(pessoa2)
ListaPessoasHash.adicionarLista(pessoa3)

print("teste")

cpfRetornado = ListaPessoasHash.procurarCpf(12345678912)

print(cpfRetornado.nome)
