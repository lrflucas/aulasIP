#%%

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

#! BOA PARTE PEGUEI DO GITHUB

notas = 4
alunos = 10
medias = []
media_sete = 0

for i in range(alunos):
    media = 0
    for j in range(notas):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= notas
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\n")
print("A média dos alunos foi:")
for i in range(alunos):
    print(f"Aluno {i+1}: {medias[i]}")

print("\n")
print(f"{media_sete} alunos tiveram média maior ou igual a 7.")

# %%