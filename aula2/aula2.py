#%%

x = int()

while x < 1000:
    print(x)
    x += 1

#%%

for numero in range(1, 11):
    print(numero)

#%%

lista_itens = ["feijão", "arroz", "carne"]

for item in lista_itens:
    print("O item agora é: " + item) 

# %%

nomes = ["João", "Maria", "Pedro", "Ana"]

for nome in nomes:
    print(f"Olá, {nome}!")

# %%

# Escreva um algoritmo para imprimir os números de 1 (inclusive) a 10 (inclusive) em ordem crescente

for numero in range(1, 11):
    print(numero)

#%%

# Faça um programa que converta metros para centímetros

numero = float(input("Digite um número em metros: "))

for cm in numero:
    print(cm*100)

#%%

# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo
# (considere o valor zero como positivo)

numero = float(input("Digite um número: "))

while numero >= 0:
    print("Positivo")
    break
else:
    print("Negativo")
    
# %%
