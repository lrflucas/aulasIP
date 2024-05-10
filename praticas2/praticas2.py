#%%

# Crie uma função Media

def calcular(n1, n2, media):
    media = (n1+n2 / len(media))   

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = float()
 
print(calcular(n1, n2, media))
#%%

# Crie uma função IMC