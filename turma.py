class Turma:
    def __init__(self):
        self.turma = []

    def cadastrarAlunos(self, alunos):
        if not alunos:
            return  

        self.menorNota = alunos[0]  
        self.maiorNota = alunos[0]  

        for i in alunos:
            self.turma.append(i)
            if i.nota < self.menorNota.nota:
                self.menorNota = i
            if i.nota > self.maiorNota.nota:
                self.maiorNota = i


    def mostrarAlunos(self):
        print('Quantidade de alunos:', len(self.turma))
        for x in self.turma:
            print(x.mostrarAluno())


