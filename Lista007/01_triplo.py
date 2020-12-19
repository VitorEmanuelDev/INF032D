# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando
# entrar com o numero 999;

n = int(input("Informe uma quantidade de números que gostaria determinar:"))

lista = []
resposta = ""

print("Informe o valor de cada número:")
for i in range(0, n):
    valor = int(input())
    lista.append(valor)

i = 0

while resposta != 999:
    print(lista[i] * 3)
    i += 1
    if i == n:
        resposta = int(input("Deseja continuar?"))
        if resposta == 999:
            print("Até mais!")
        else:
            i = 0