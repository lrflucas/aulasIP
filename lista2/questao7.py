#%%

# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

conta = int(input("Digite o número da sua conta: "))
saldo = float(input("Digite seu saldo: "))
debito = float(input("Digite quanto você tem no débito: "))
credito = float(input("Digite quanto você tem no crédito: "))
saldoatual = (saldo - (debito + credito))

print(f"Número da conta: {conta}")
print(f"Saldo: {saldo}")
print(f"Quantidade de débito: {debito}")
print(f"Quantidade de crédito: {credito}")

if saldoatual >= 0:
    print(f"Seu saldo atual é {saldoatual}.")
    print("Saldo Positivo!")
else:
    print(f"Seu saldo atual é {saldoatual}.")
    print("Saldo Negativo!")

# %%