#%%

# Ler as notas da 1a. e 2a. avaliações de um aluno.
# Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado
# (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
media = ((n1+n2)/2)

if media >= 6:
    print(f"Você foi aprovado! Sua média foi {media}.")
else:
    print(f"Você foi reprovado. Sua média foi {media}.")
    
# %%
