#1. que entre com um número e informe se o mesmo está compreendido entre 20 e 90;

print("Informe um número")
numero = int(input())

if 20 < numero < 90:
    print(numero, "está contido entre 20 e 90")
else:
    print(numero, "não está contido entre 20 e 90")