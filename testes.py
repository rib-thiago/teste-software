import unittest

import aluno as a
import turma as t


class turmaTest(unittest.TestCase):
    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = []

        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', 6))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 7))

        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(
            10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota'
        )

    def testMenor(self):
        self.assertEqual(
            6, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota'
        )

    def testIntervalo(self):
        print('Testar se o intervalo de notas está correto.')
        self.assertGreaterEqual(
            self.turmaObject.menorNota.nota, 9, 'Nota menor está abaixo de 0'
        )
        self.assertLessEqual(
            self.turmaObject.maiorNota.nota, 10, 'Nota maior está acima de 10'
        )


if __name__ == '__main__':
    unittest.main()
