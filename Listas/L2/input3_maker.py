from random import randint as rint

for i in range(2):
    linha = []
    for j in range(100000):
        linha.append(rint(-100000, 100000))

    print(' '.join(str(e) for e in linha))

# comando py input3_maker.py > input3.txt usado
# input aleatorio usado para testar 2-Validando_as_Sequencias.py
