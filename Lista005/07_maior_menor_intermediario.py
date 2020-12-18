#7.entrar com 3 números e armazená-los em três variáveis diferentes:
#maior, menor e intermediário

numeros = []

print("Informe três números:")

for i in range(0, 3):
    numero = int(input())

    numeros.append(numero)

#numeros = sorted(numeros)
numeros.sort()

menor = numeros[0]
intermediario = numeros[1]
maior = numeros[2]

print("menor:", menor)
print("intermediário:", intermediario)
print("maior:", maior)
