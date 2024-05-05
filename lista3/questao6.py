#%%

# Seja criativo ao desenvolver este programa.
    # a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
    # b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
    # c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites.
    #    Imprima o nome das pessoas que não poderão comparecer.
    # d. Modifique sua lista, substitua os desistentes por novos convidados.
    # e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ["Cristiano Ronaldo", "LeBron James", "Jaden Smith", "Josh Dun", "Kendrick Lamar"]

for nome in convidados:
    print(f"Sr. {nome}, você está convidado para um jantar às 20h, no dia 30/04, na minha casa.")

print("\n")

convidados.remove("Cristiano Ronaldo")
print("Não poderá comparecer: Cristiano Ronaldo")

print(convidados)

print("\n")

convidados.insert(4, "21 Savage")

for nome in convidados:
    print(f"Sr. {nome}, devido ao cancelamento repentino do sr. Cristiano Ronaldo, estou reenviando o convitepara um jantar às 20h, no dia 30/04, na minha casa.")

# %%