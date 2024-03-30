import pessoa

class HashPessoas:
    def __init__(self, tamanhoLista : int):
        self.tamanholista = tamanhoLista
        self.lista = [None for c in range(tamanhoLista)]
    
    def adicionarLista(self, pessoa : pessoa):
        pessoaAdicionar = pessoa
        cpf = pessoaAdicionar.cpf
        posicaoPessoa = self.hashCpf(cpf)

        while self.lista[posicaoPessoa] != None and self.lista[posicaoPessoa].cpf != cpf:
            posicaoPessoa = self.rehashCpf(posicaoPessoa)

        self.lista[posicaoPessoa] = pessoa

    def procurarCpf(self, cpf):
        return self.lista[self.hashCpf(cpf)]

    def hashCpf(self, cpf):
        cpfhashado = 0
        cpf_str = str(cpf)

        for c in range(0, len(cpf_str),2):
            agrupar = cpf_str[c:c+2]
            cpfhashado += int(agrupar)

        cpfhashado %= 11

        return cpfhashado

    def rehashCpf(self, antigoHash):
        return (antigoHash+1) % self.tamanholista
