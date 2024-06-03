#Desafio Tupla

aluno1 = ('Gabriel', [7.2, 8.4, 5.5, 10])
aluno2 = ('Flávio', [8.2, 8, 7, 6.7])
aluno3 = ('Amanda', [10, 7.2, 6.9, 8])
aluno4 = ('Bruna', [9.2, 7.4, 6.7, 7])

#Imprimir os alunos em ordem decrescente da maior MÉDIA para a menor

media1= sum(aluno1[1])/4
media2= sum(aluno2[1])/4
media3= sum(aluno3[1])/4
media4= sum(aluno4[1])/4

alunos = [(aluno1[0], media1), (aluno2[0], media2), (aluno3[0], media3), (aluno4[0], media4)]

print(alunos)

alunos.sort(key=lambda aluno:aluno[1], reverse=True)