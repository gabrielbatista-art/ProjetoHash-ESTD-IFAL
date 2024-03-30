class buscaSequencial:
    def __init__(self):
        self.lista = []
    
    def adicionarLista(self, pessoa):
        self.lista.append(pessoa)
    
    def buscarNaLista(self, pessoaCpf):
        for pessoa in self.lista:
            if pessoa.cpf == pessoaCpf:
                return pessoa
        else:
            print("Pessoa Não Encontrada")
