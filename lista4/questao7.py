#%%

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   1. o produto do dobro do primeiro com metade do segundo .
#   2. a soma do triplo do primeiro com o terceiro.
#   3. o terceiro elevado ao cubo.

numint1 = int(input("Digite um número inteiro: "))
numint2 = int(input("Digite outro número inteiro: "))
numreal = float(input("Digite um número real: "))

print(f"Primeiro número: {numint1}")
print(f"Segundo número: {numint2}")
print(f"Terceiro número: {numreal}\n")

print(f"Dobro do primeiro: {numint1 * 2}")
print(f"Metade do segundo: {numint2 / 2}")
print(f"Produto do dobro do primeiro com metade do segundo: {(numint1 * 2) * (numint2 / 2)}\n")

print(f"Triplo do primeiro: {numint1 * 3}")
print(f"Soma do triplo do primeiro com o terceiro: {(numint1 * 3) + numreal}\n")

print(f"Terceiro elevado ao cubo: {numreal ** 3}")

# %%