#%%

import math
from math import pi

# Calculando a raiz quadrada de 9
numero = 52
raiz_quadrada = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

# %%

# def soma(parametro1, parametro2):
#    return(parametro1 + parametro2)

def calcular(numero1, numero2, operacao):

  if operacao == "+":
    resultado = numero1 + numero2
  elif operacao == "-":
    resultado = numero1 - numero2
  elif operacao == "*":
    resultado = numero1 * numero2
  elif operacao == "/":
    resultado = numero1 / numero2
  else:
    resultado = "Operação inválida!"

  return resultado


# Chamada da função
operacao = input("Digite a operação desejada (+, -, *, /): ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = calcular(numero1, numero2, operacao)
print(f"O resultado da operação {operacao} é: {resultado}")


# %%

idade = int(input("Digite sua idade: "))
classificar_idade(idade)

def classificar_idade(idade):
    """
  Função que classifica a idade em categorias.

  Argumento:
    idade (int): Idade da pessoa.
  """
    if idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 18:
        categoria = "Adolescente"
    elif 19 <= idade <= 65:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    print(f"Sua categoria de idade é: {categoria}")

#%%

import requests

def converter_para_dolares(valor_reais):

   # Obter taxa de câmbio atual
   url = "https://api.exchangerate-api.com/v4/latest/BRL"
   response = requests.get(url)
   data = response.json()
   taxa_cambio = data["rates"]["USD"]

   # Converter reais para dólares
   valor_dolares = valor_reais * taxa_cambio

   return valor_dolares

valor_reais = float(input("Digite o valor em reais: "))

valor_dolares = converter_para_dolares(valor_reais)
print(f"O valor equivalente em dólares é: ${valor_dolares:.2f}")

# %%
