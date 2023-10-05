"""Este módulo contém a classe Turma que representa uma turma de alunos."""


class Turma:
    """Classe que representa uma turma de alunos."""

    def __init__(self):
        """Inicializa uma nova instância da classe Turma."""
        self.turma = []

    def cadastrarAlunos(self, alunos):
        """
        Cadastra alunos na turma e atualiza as menores e maiores notas.

        Args:
            alunos (list): Uma lista de objetos Aluno a serem cadastrados.

        Returns:
            None
        """
        if not alunos:
            return

        self.menorNota = alunos[0]
        self.maiorNota = alunos[0]

        for i in alunos:
            if i.nota >= 0 and i.nota <= 10:
                self.turma.append(i)
                if i.nota < self.menorNota.nota:
                    self.menorNota = i
                elif i.nota > self.maiorNota.nota:
                    self.maiorNota = i

    def mostrarAlunos(self):
        """
        Mostra informações sobre a turma, incluindo a quantidade de alunos e seus dados.

        Returns:
            None
        """
        print('Quantidade de alunos:', len(self.turma))
        for x in self.turma:
            print(x.mostrarAluno())
