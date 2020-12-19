#4) Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#a.Álcool:
#b.até 20 litros, desconto de 3% por litro
#c.acima de 20 litros, desconto de 5% por litro
#d.Gasolina:
#e.até 20 litros, desconto de 4% por litro
#f.acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
#pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
#é R$ 1,90.

combustivel = input("Álcool (A) ou Gasolina (G)?")
volume = float(input("Quantos litros?"))

combustivel = combustivel.lower()

if combustivel == "a":
    preco = 1.9 * volume
    if volume <= 20:
        desconto = .97 * preco
        print("Valor a ser pago: R$", round(desconto, 2))
    else:
        desconto = .95 * preco
        print("Valor a ser pago: R$", round(desconto, 2))
elif combustivel == "g":
    preco = 2.5 * volume
    if volume <= 20:
        desconto = .96 * preco
        print("Valor a ser pago: R$", round(desconto, 2))
    else:
        desconto = .94 * preco
        print("Valor a ser pago: R$", round(desconto, 2))
else:
    print("Opção inválida.")
