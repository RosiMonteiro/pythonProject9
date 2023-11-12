class Aluno:
    def __init__(self, nome,  idade, curso, matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setCurso(self, curso):
        self.curso = curso

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCurso(self):
        return self.curso

    def getMatricula(self):
        return self.matricula

    def ExibirInformacoesPadrãoDeAluno(self):
        print(self.nome, self.idade, self.curso, self.matricula)

alunoPadrão1 = Aluno('Rosicleite Monteiro','38', 'Python', '123456789')
alunoPadrão1.ExibirInformacoesPadrãoDeAluno()
alunoPadrão2 = Aluno('Eli Monteiro', '39', 'Java', '789456123')
alunoPadrão2.ExibirInformacoesPadrãoDeAluno()


while True:

        continuar = 'c'
        sair = 's'

        nome = str(input('Nome do Aluno:'))
        idade = int(input('idade do Aluno:'))
        curso = str(input('Curso do Aluno:'))
        matricula = str(input('Matricula do Aluno:'))


        class Alunoo:

                def __init__(self, nome = nome, idade = idade, curso = curso, matricula = matricula):
                    self.nome = nome
                    self.idade = idade
                    self.curso = curso
                    self.matricula = matricula


                def setIdade(self, idade):
                    self.idade = idade


                def setNome(self, nome):
                    self.nome = nome


                def setCurso(self, curso):
                    self.curso = curso


                def setMatricula(self, matricula):
                    self.matricula = matricula


                def getNome(self):
                    return self.nome


                def getIdade(self):
                    return self.idade


                def getCurso(self):
                    return self.curso


                def getMatricula(self):
                    return self.matricula


                def ExibirInformacoesPersonalizadasDeAluno(self):
                    print(self.nome, self.idade, self.curso, self.matricula)

        alunoPersonalizado = Alunoo()
        alunoPersonalizado.ExibirInformacoesPersonalizadasDeAluno()

        continuar = input('Para sair Digite: (S) ou Digite (C) para Continuar :')
        print(continuar)

        if continuar == 'c':
            print('Digite os Dados do Proximo Aluno:')

        else:
            print('Até Breve:')
            break
