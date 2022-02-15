class Aluno:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__nota1 = -1.1
        self.__nota2 = -1.2
        self.__nota3 = -1.3

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def inicializar_nota(self, nota, numero_prova):
        if numero_prova == 1:
            self.__nota1 = nota
        elif numero_prova == 2:
            self.__nota2 = nota
        elif numero_prova == 3:
            self.__nota3 = nota
        else:
            print('digite 1, 2 ou 3.')

    def verifica_situacao_media(self):
        if self.__nota1 >=0 and self.__nota2 >=0 and self.__nota3 >=0:
            mean = ((self.__nota3 + self.__nota2 + self.__nota1) / 3)
            if mean >= 7:
                return True
            else:
                return False
        else:
            print('Ainda faltam provas a serem feitas.')
            return False

    def imprime_informacoes(self):
        notas = [self.__nota1, self.__nota2, self.__nota3]
        for nota in range(len(notas)):
            if notas[nota] < 0:
                notas[nota] = (f'nota {nota+1} nao fornecida')
        print(f'Nome: {self.__nome}\nCPF: {self.__cpf}\nNota 1: {notas[0]}'
              f'\nNota 2:{notas[1]}\nNota 3: {notas[2]}\n')

def procura_aluno():
    aluno = input('Digite nome aluno:\n')
    for i in alunos:
        if i.get_nome() == aluno:
            return i
        else:
            print('Aluno nao encontrado.')
def menu():
    print('___' * 9+'\n')
    print('1 - Adicionar Aluno')
    print("2 - Inserir Nota")
    print("3 - Verifica media")
    print("4 - Imprime informacoes")
    print('5 - Encerrar\n')
    entrada = input()
    if entrada == '5':
        return print('Encerrado.')
    else:
        if entrada == '1':
            print('....' * 9)
            nome_aluno = input('Digite o nome do aluno')
            cpf_aluno = input('Digite o CPF do aluno')
            alunos.append(Aluno(nome_aluno, cpf_aluno))
        elif entrada == '2':
            print('....' * 9)
            num_prova = input('Digite o numero da prova:\n')
            nota_prova = input('Digite a nota nesta prova:\n')
            aluno = procura_aluno()
            aluno.inicializar_nota(nota_prova, num_prova)
            print('Nota editada com sucesso.')
        elif entrada == '3':
            print('....' * 9)
            aluno = procura_aluno()
            media = aluno.verifica_situacao_media()
            if media:
                print('passou')
            else:
                print('num passou ou n tem todas as notas.')
        elif entrada == '4':
            print('....' * 9)
            aluno = procura_aluno()
            aluno.imprime_informacoes()
        return menu()

alunos = []

if __name__ == '__main__':
    Aluno('Jurema', 546546545)
    menu()