#%%

# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 > n2:
    print(f"{n2}, {n1}")
else:
    print(f"{n1}, {n2}")

# %%