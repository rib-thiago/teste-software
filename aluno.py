"""Módulo contendo a classe Aluno."""


class Aluno:
    """Classe que representa um aluno com nome, sobrenome e nota."""

    def __init__(self, nome, sobrenome, nota):
        """
        Inicializa uma nova instância da classe Aluno.

        Args:
            nome (str): O nome do aluno.
            sobrenome (str): O sobrenome do aluno.
            nota (float): A nota do aluno.

        Returns:
            None
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        """
        Retorna uma representação em string do aluno.

        Returns:
            str: Uma string formatada com nome, sobrenome e nota do aluno.
        """
        return (
            'Aluno: '
            + self.nome
            + ' '
            + self.sobrenome
            + ' - Nota: '
            + str(self.nota)
        )
