"""
Exemplo de uso das classes Aluno e Turma para cadastrar alunos.

Contém métodos para encontrar a menor e a maior nota, e mostrar informações
sobre a turma.
"""


import aluno as a
import turma as t

alunos = []
alunos.append(a.Aluno('Fabio', 'Teixeira', 8))
alunos.append(a.Aluno('Fabiano', 'Teixeira', 10))
alunos.append(a.Aluno('Melissa', 'Teixeira', -1))

turmaObject = t.Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print('*' * 30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
