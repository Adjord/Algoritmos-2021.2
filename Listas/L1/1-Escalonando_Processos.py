class Processo:
    def __init__(self, id_init, tempo_init):
        self.id = id_init
        self.tempo = tempo_init
        self.proximo = None

    def get_id(self):
        return self.id

    def get_tempo(self):
        return self.tempo

    def get_prox(self):
        return self.proximo

    def muda_tempo(self, x):
        self.tempo = x

    def muda_prox(self, processo):
        self.proximo = processo


class Processador():
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, processo):
        if self.first is not None:
            self.first, self.last = processo
        else:
            self.last.muda_prox(processo)
            processo.muda_prox(None)
            self.last = processo

    def delete(self):
        proc = self.first
        if proc.get_prox() is not None:
            self.first = proc.get_prox()
            proc.muda_prox(None)
        else:



def exe(tempo):
    processo = l_first()
    processo_tempo = processo.get_tempo()
    processo_id = processo.get_id()
    if processo.get_tempo() > tempo:
        print('O programa {0} executou por {1} segundos.'.format(processo_id, tempo))
        processo_tempo -= tempo
        processo.muda_tempo(processo_tempo)
        l_insert(processo)
        tempo = 0
    else:
        print('O programa {0} executou por {1} segundos.'.format(processo_id, processo_tempo))
        print('O programa {0} terminou.'.format(processo_id))
        tempo -= processo.get_tempo()
        l_del()
    if tempo > 0:
        exe(tempo)


def em_linha():
    procs = 1
    proc = l_first()
    if proc is not None:
        while proc.get_prox() is not None:
            procs += 1
            proc = proc.get_prox()
    else:
        procs = 0
    return procs


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


def main(x, count=0):
    count += 1
    entrada = trata_entrada(input())
    if entrada[0] == 'ADD':
        id_processo = entrada[1]
        tempo_processo = int(int(entrada[2]))
        processo = Processo(id_processo, tempo_processo)
        l_insert(processo)
        print('O programa {0} foi agendado com sucesso!'.format(processo.get_id(),))
    else:
        tempo = int(entrada[1])
        exe(tempo)
        proxs = em_linha()
        print('A linha possui {0} programas.'.format(proxs))
    if count != x:
        main(x, count)


processos = []
if __name__ == '__main__':
    sentinel = Processo(None, None)
    sentinel.muda_prox(None)
    processos.append(sentinel)
    numEntradas = input()
    main(int(numEntradas))
