from geradorNomes import generate_word
from random import randint

class Pessoas():
    def __init__(self, cpf = None, nome = None, telefone = None, senha = None):
        if cpf == None:
            self.cpf = self.gerarCpf()
        else:
            self.cpf = cpf
            
        if nome == None:
            self.nome = 'self.gerarNome()'
        else:
            self.nome = nome

        if telefone == None:
            self.telefone = randint(10000000000, 99999999999)
        else:
            self.telefone = telefone

        if senha == None:
            self.senha = randint(100000, 999999)
        else:
            self.senha = senha

    def gerarCpf(self):
        randNum = randint(100000000, 999999999)
        proibidos = ['000000000', '111111111', '222222222', '333333333', '444444444', '555555555', '666666666', '777777777', '888888888', '999999999']
        cpfFinal = 0

        while randNum in proibidos or len(str(randNum)) != 9:
            randNum = randint(100000000, 999999999)
        
        randNum = self.validarCpf(randNum)

        return randNum

    def validarCpf(self, cpfIncompleto):
        soma = 0
        digitos = str(cpfIncompleto)
        for i in range(9):
            soma += int(digitos[i]) * (10 - i)

        digito1 = 11 - (soma % 11)
        if digito1 >= 10:
            digito1 = 0

        soma = 0
        for i in range(9):
            soma += int(digitos[i]) * (11 - i)

        soma += digito1 * 2
        digito2 = 11 - (soma % 11)
        if digito2 >= 10:
            digito2 = 0

        return int(digitos + str(digito1) + str(digito2))


    def gerarNome(self):
        primeiroNome = generate_word(randint(5, 9))
        segundoNome = generate_word(randint(5, 9))
        return f"{primeiroNome} {segundoNome}"
    