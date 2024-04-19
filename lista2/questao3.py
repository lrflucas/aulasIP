#%%

# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade = int(input("Digite quantas maçãs irá comprar: "))

if quantidade < 12:
    maçã = 1.30
    print(f"{quantidade} maçãs compradas.")
    calculo = (quantidade * maçã)
    print(f"O custo total é {calculo}.")
else:
    maçã = 1.00
    print(f"{quantidade} maçãs compradas.")
    calculo = (quantidade * maçã)
    print(f"O custo total é {calculo}.")

# %%
