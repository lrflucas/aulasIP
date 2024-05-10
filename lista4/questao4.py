#%%

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganhohora = float(input("Digite quanto você ganha por hora: "))
horas = int(input("Digite o número de horas trabalhadas no mês: "))
meses = int(input("Digite quantos dias tem o mês que você quer saber o salário: "))

if meses == 28:
    print(f"Você ganha R${ganhohora*horas} em um mês com {meses} dias.")
elif meses == 29:
    print(f"Você ganha R${ganhohora*horas} em um mês com {meses} dias.")
elif meses == 30:
    print(f"Você ganha R${ganhohora*horas} em um mês com {meses} dias.")
elif meses == 31:
    print(f"Você ganha R${ganhohora*horas} em um mês com {meses} dias.")
else:
    print("Impossível calcular, mês inválido.")
    
# %%
