#12. Entrar com dois números inteiros e efetuar a adição. Caso o valor somado seja maior que 20, este
#deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este
#deverá ser apresentado subtraindo-se 5.

print("Informe dois inteiros:")
numero_01 = int(input())
numero_02 = int(input())

soma = numero_01 + numero_02

if soma > 20:
    soma = soma + 8
    print("Resultado:", soma)
else:
    soma = soma - 5
    print("Resultado:", soma)