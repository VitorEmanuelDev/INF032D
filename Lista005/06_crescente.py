#6.entrar com 3 números e imprimi-los em ordem crescente

numeros = []

print("Informe três números:")

for i in range(0, 3):
    numero = int(input())

    numeros.append(numero)

#numeros = sorted(numeros)
numeros.sort()
print(numeros)
