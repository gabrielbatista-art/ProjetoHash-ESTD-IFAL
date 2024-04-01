from random import randint

def hashCpf(cpf):
        cpfhashado = 0
        cpf_str = str(cpf)

        for c in range(0, len(cpf_str),2):
            agrupar = cpf_str[c:c+2]
            cpfhashado += int(agrupar)

        cpf %= 1000003

        # cpfhashado = (135+1) % 1000001

        print(cpfhashado)

        return cpfhashado

print(hashCpf(randint(10000000000, 99999999999)))
