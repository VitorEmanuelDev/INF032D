#10.Criar um programa que deixe entrar com 10 números positivos e imprima a raiz
#quadrada de cada numero. para cada entrada de dados devera haver um trecho de
#"proteção" para que um numero negativo não seja aceito.

n = 10
lista_raiz = []
i = 0

while i < n:
    numero = float(input("Informe um número:"))
    if numero > 0:
        raiz = round(numero ** .5, 2)
        lista_raiz.append(raiz)
        i += 1
    else:
        print("Tente nvamente, mas informe um número positivo.")

print("Raízes:")
print(lista_raiz)