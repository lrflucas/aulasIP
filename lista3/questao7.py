#%%

# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.


usuarios = []

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu e-mail: ")

usuario = {
    "Nome": nome,
    "Idade": idade,
    "Email": email
}

usuarios.append(usuario) # append adiciona só uma vez

for novousuario in usuarios:
    print("Nome: ", usuario["Nome"])
    print("Idade: ", usuario["Idade"])
    print("E-mail: ", usuario["Email"])
    print("\n")

# %%