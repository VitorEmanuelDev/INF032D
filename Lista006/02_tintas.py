#2) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que
#custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
#em 3 situações:

# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
#sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

tamanho = float(input("Informe o tamanho da área a ser pintada:"))

lata = 18
galao = 3.6

tamanho_lata = 6 * lata
tamanho_galao = 6 * galao


if tamanho >= tamanho_lata:
    resto_lata = int(tamanho % tamanho_lata)
    tamanho_certo = tamanho - resto_lata
    latas = math.ceil(tamanho_certo / tamanho_lata)
    custo = float(latas * 80)

    if resto_lata == 0:
        print("O custo da pintura será de: R$", custo)
        print("Você vai precisar de", latas,"latas")

    if resto_lata != 0 and resto_lata <= tamanho_galao * 3:
        galoes = math.ceil(float(resto_lata / tamanho_galao))
        custo_complementar = galoes * 25
        custo = custo_complementar + custo
        print("O custo da pintura será de: R$", custo)
        print("Você vai precisar de", latas, "latas e de", galoes," galões")


if tamanho_galao * 3 < tamanho <= tamanho_lata:
    latas = math.ceil(float(tamanho / tamanho_lata))
    custo = latas * 80
    print("O custo da pintura será de: R$", custo)
    print("Você vai precisar de", latas, "lata")

if tamanho <= tamanho_galao * 3:
    galoes = math.ceil(float(tamanho / tamanho_galao))
    custo = galoes * 25
    print("O custo da pintura será de: R$", custo)
    print("Você vai precisar de", galoes, "galões")
