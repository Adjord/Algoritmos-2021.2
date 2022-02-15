class Prato:
    def __init__(self, int_init):
        self.num = int_init
        self.abaixo = None

    def get_num(self):
        return self.num

    def get_prox(self):
        return self.abaixo

    def muda_prox(self, x):
        self.abaixo = x


class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, n):
        prato = Prato(n)
        if self.topo is None:
            self.topo = prato
        else:
            prato.muda_prox(self.topo)
            self.topo = prato

    def pop(self):
        if self.topo is None:
            print(empty)
        else:
            prato = self.topo
            self.topo = self.topo.get_prox()
            prato.muda_prox(None)
            del prato
            if self.topo is not None:
                print(self.topo.get_num())
            else:
                print(empty)

    def get_max(self):
        if self.topo is None:
            print(empty)
        else:
            maior = -1
            prato = self.topo
            if prato.get_prox() is None:
                print(prato.get_num())
            else:
                while prato is not None:
                    if prato.get_num() > maior:
                        maior = prato.get_num()
                    prato = prato.get_prox()
                print(maior)

    def get_min(self):
        if self.topo is None:
            print(empty)
        else:
            menor = 9999999999999999
            prato = self.topo
            if prato.get_prox() is None:
                print(prato.get_num())
            else:
                while prato is not None:
                    if prato.get_num() < menor:
                        menor = prato.get_num()
                    prato = prato.get_prox()
                print(menor)


def trata_entrada(entrada):
    palavras = []
    palavra = ''
    for caractere in entrada:
        if caractere != ' ':
            palavra += caractere
        else:
            palavras.append(palavra)
            palavra = ''
    palavras.append(palavra)
    return palavras


def main(num, cont=0):
    cont += 1
    entrada = trata_entrada(input())
    if entrada[0] == 'push':
        pilha.push(int(entrada[1]))
    elif entrada[0] == 'pop':
        pilha.pop()
    elif entrada[0] == 'getMax':
        pilha.get_max()
    elif entrada[0] == 'getMin':
        pilha.get_min()
    if cont != num:
        main(num, cont)


if __name__ == '__main__':
    empty = 'empty stack'
    pilha = Pilha()
    numEntradas = input()
    main(int(numEntradas))
