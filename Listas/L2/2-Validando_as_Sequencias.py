class Elemento:
    def __init__(self, num):
        self.num = int(num)
        self.repete = False
        self.sequencia = [False, False]
        self.pai = None
        self.left = None
        self.right = None


class Lista:
    def __init__(self):
        self.raiz = None

    def inserir(self, elemento):
        aux = None
        node = self.raiz
        while node is not None:
            if elemento.num == node.num:
                node.repete = True
                return
            aux = node
            if elemento.num < node.num:
                node = node.left
            else:
                node = node.right
        elemento.pai = aux
        if aux is None:
            self.raiz = elemento
        elif elemento.num < aux.num:
            aux.left = elemento
        else:
            aux.right = elemento

    def contem_nao_contem(self, node):
        global f, t
        if node is not None:
            self.contem_nao_contem(node.left)
            if node.repete:
                t.append(node.num)
            elif node.sequencia[1]:
                f.append(node.num)
            self.contem_nao_contem(node.right)


if __name__ == '__main__':
    sequencias = Lista()
    for i in range(2):
        for j in input().split():
            numero = Elemento(j)
            numero.sequencia[i] = True
            sequencias.inserir(numero)
    t = []
    f = []
    sequencias.contem_nao_contem(sequencias.raiz)
    print(' '.join(str(e) for e in t))
    print(' '.join(str(e) for e in f))
