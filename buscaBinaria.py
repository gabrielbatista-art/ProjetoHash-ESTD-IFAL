from pessoa import Pessoas

class BuscaBinaria:
    
    def __init__(self):
        self.lista = []
    
    def add(self,pessoa):
        self.lista.append(pessoa)
        # listaOrdenada = sorted(self.lista, key=lambda pessoa: pessoa.cpf)
        # self.lista = listaOrdenada

    def busca_bi(self,cpf):
        listaOrdenada = sorted(self.lista, key=lambda pessoa: pessoa.cpf)
        self.lista = listaOrdenada

        lista_cpf = self.lista
        primeiro = 0
        ultimo = len(lista_cpf) - 1
        encontrou = False

        while primeiro <= ultimo and not encontrou:
            meio = (primeiro + ultimo)//2
            if lista_cpf[meio].cpf == cpf:
                return lista_cpf[meio]
            else:
                if lista_cpf[meio].cpf > cpf:
                    ultimo = meio-1
                else:
                    primeiro = meio+1
