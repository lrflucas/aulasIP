#%%

# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

#! TIVE AJUDA DE IA

alunos = [(17, 1.75), (18, 1.75), (14, 1.55), (12, 1.47), (11, 1.35), (19, 1.72), (15, 1.53), (13, 1.42), (17, 1.73), (11, 1.40),
          (16, 1.70), (18, 1.72), (12, 1.50), (18, 1.80), (20, 1.75), (15, 1.66), (17, 1.70), (11, 1.25), (13, 1.49), (19, 1.75), 
          (14, 1.52), (16, 1.68), (15, 1.65), (20, 1.90), (12, 1.51), (14, 1.58), (19, 1.68), (17, 1.77), (12, 1.51), (13, 1.57)]

alturatotal = sum(altura for _, altura in alunos)
alturamedia = alturatotal / len(alunos)
contador = sum(1 for idade, altura in alunos if idade > 13 and altura < alturamedia)

print(f"Quantidade de alunos maiores de 13 anos e altura inferior à média: {contador}")

# %%