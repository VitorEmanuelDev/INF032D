#10.Criar um programa que deixe entrar com 10 números positivos e imprima a raiz
#quadrada de cada numero. para cada entrada de dados devera haver um trecho de
#"proteção" para que um numero negativo não seja aceito.

n = 10
lista_raiz = []

for i in range(0, 10):
    numero = float(input("Informe um número:"))
    if numero < 0:
        numero = numero * -1
    raiz = round(numero ** .5, 2)
    lista_raiz.append(raiz)

print("Raízes:")
print(lista_raiz)