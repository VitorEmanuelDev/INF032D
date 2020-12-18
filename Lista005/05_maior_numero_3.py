#5.Entrar com 3 números, e imprimir o maior número

print("Informe três números:")
numero_01 = int(input())
numero_02 = int(input())
numero_03 = int(input())

if numero_01 > numero_02 and numero_01 > numero_03:
    print("Maior:", numero_01)
elif numero_02 > numero_01 and numero_02 > numero_03:
    print("Maior:", numero_02)
elif numero_03 > numero_01 and numero_03 > numero_02:
    print("Maior:", numero_03)