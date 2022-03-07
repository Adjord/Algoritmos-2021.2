class Jogador:
    def __init__(self, num, nome):
        self.num = int(num)
        self.nome = nome
        self.pai = None
        self.left = None
        self.right = None


class Arvere:
    def __init__(self):
        self.raiz = None

    def inserir(self, elemento):
        aux = None
        node = self.raiz
        while node is not None:
            if elemento.num == node.num:
                return False
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
        return True

    def pesquisa(self, node, elemento):
        if node is None or elemento == node.num:
            return node
        if elemento < node.num:
            return self.pesquisa(node.left, elemento)
        else:
            return self.pesquisa(node.right, elemento)

    def minimo(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maximo(self, node):
        while node.right is not None:
            node = node.right
        return node

    def sucessor(self, node):
        if node.right is not None:
            return self.minimo(node.right)
        aux = node.pai
        while aux is not None and node == aux.right:
            node = aux
            aux = aux.pai
        return aux

    def antecessor(self, node):
        if node.left is not None:
            return self.maximo(node.left)
        aux = node.pai
        while aux is not None and node == aux.left:
            node = aux
            aux = aux.pai
        return aux

    def proxs(self, valor):
        node = self.pesquisa(self.raiz, valor)
        suc = self.sucessor(node)
        ant = self.antecessor(node)
        if ant is None and suc is None:
            print('Apenas {0} existe no sistema...'.format(node.nome))
        elif ant is None:
            print('{0} e o menor! e logo apos vem {1}'.format(node.nome, suc.nome))
        elif suc is None:
            print('{0} e o maior! e logo atras vem {1}'.format(node.nome, ant.nome))
        else:
            print('{0} vem apos {1} e antes de {2}'.format(node.nome, ant.nome, suc.nome))


def menu():
    jogadores = Arvere()
    entradas = int(input())
    for comando in range(0, entradas):
        entrada = input()
        if entrada[:3] == 'ADD':
            parametros = entrada.split()
            elemento = Jogador(int(parametros[2]), parametros[1])
            inseriu = jogadores.inserir(elemento)
            if inseriu:
                print('{0} inserido com sucesso!'.format(parametros[1]))
            else:
                print('{0} ja esta no sistema.'.format(parametros[1]))
        elif entrada[:4] == 'PROX':
            jogadores.proxs(int(entrada.split()[1]))


if __name__ == '__main__':
    menu()
