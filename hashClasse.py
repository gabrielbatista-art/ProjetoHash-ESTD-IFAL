import pessoa

class HashPessoas:
    def __init__(self, tamanhoLista : int):
        self.tamanholista = tamanhoLista
        self.lista = [None] * tamanhoLista
        self.contadorRehash = 0
        self.contadorAdicoes = 0

    
    def adicionarLista(self, pessoa : pessoa):
        pessoaAdicionar = pessoa
        cpf = pessoaAdicionar.cpf
        posicaoPessoa = self.hashCpf(cpf)

        while True:
            if self.lista[posicaoPessoa] == None:
                self.lista[posicaoPessoa] = pessoa
                # print("Add")
                return
            else:
                if self.lista[posicaoPessoa].cpf != cpf:
                    posicaoPessoa = self.rehashCpf(posicaoPessoa)

        # self.lista[posicaoPessoa] = pessoa

        # self.contadorAdicoes += 1
        # print(f"Adicionou = {self.contadorAdicoes}")


    def procurarCpf(self, cpf):
        posicao = self.hashCpf(cpf)
        while self.lista[posicao].cpf != cpf:
            posicao = self.rehashCpf(posicao)

        return self.lista[posicao]


    def hashCpf(self, cpf):
        cpfhashado = 0
        cpf_str = str(cpf)

        for c in range(0, len(cpf_str),2):
            agrupar = cpf_str[c:c+2]
            cpfhashado += int(agrupar)

        cpfhashado %= self.tamanholista

        return cpfhashado

    def rehashCpf(self, antigoHash):
        # print(f"Rehashou {self.contadorRehash}")
        self.contadorRehash += 1
        return (antigoHash+1) % self.tamanholista
