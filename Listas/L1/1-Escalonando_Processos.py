class Processo:
    def __init__(self, id_init, tempo_init):
        self.id = id_init
        self.tempo = tempo_init
        self.proximo = None
        self.anterior = None

    def get_id(self):
        return self.id

    def get_tempo(self):
        return self.tempo

    def get_prox(self):
        return self.proximo

    def get_ant(self):
        return self.anterior

    def muda_tempo(self, x):
        self.tempo = x

    def muda_prox(self, processo):
        self.proximo = processo

    def muda_ant(self, processo):
        self.anterior = processo

    def delete(self):
        self.anterior = None
        self.proximo = None


class Processador:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, id_proc, tempo):
        processo = Processo(id_proc, tempo)
        if self.first is None:
            self.first = processo
        else:
            self.last.muda_prox(processo)
            processo.muda_ant(self.last)
        self.last = processo

    def delete(self):
        proc = self.first
        nexts = proc.get_prox()
        if nexts is None:
            proc.delete()
            self.first = None
            self.last = None
            del proc
        else:
            nexts.muda_ant(None)
            proc.delete()
            self.first = nexts
            del proc

    def exec(self, tempo):
        proc = self.first
        if proc is None:
            return None
        proc_tempo = proc.get_tempo()
        proc_id = proc.get_id()
        if proc_tempo > tempo:
            print('O programa {0} executou por {1} segundos.'.format(proc_id, tempo))
            proc_tempo -= tempo
            self.delete()
            self.insert(proc_id, proc_tempo)
            tempo = 0
        else:
            print('O programa {0} executou por {1} segundos.'.format(proc_id, proc_tempo))
            print('O programa {0} terminou.'.format(proc_id))
            tempo -= proc_tempo
            self.delete()
        if tempo > 0:
            self.exec(tempo)

    def retorna_processos(self):
        proc = self.first
        prox = 0
        while proc is not None:
            prox += 1
            proc = proc.get_prox()
        return prox


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
        processador.insert(id_processo, tempo_processo)
        print('O programa {0} foi agendado com sucesso!'.format(id_processo))
    else:
        tempo = int(entrada[1])
        processador.exec(tempo)
        proxs = processador.retorna_processos()
        print('A linha possui {0} programas.'.format(proxs))
    if count != x:
        main(x, count)


if __name__ == '__main__':
    processador = Processador()
    numEntradas = input()
    main(int(numEntradas))
