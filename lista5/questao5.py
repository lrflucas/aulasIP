#%%

# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

#! BOA PARTE PEGUEI DO GITHUB

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

print("Os números foram: ")
for numero in numeros:
   print(numero)

# %%