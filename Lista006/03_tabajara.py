#3) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#Até 5 Kg
#Acima de 5 Kg

#File Duplo
#R$ 4,90 por Kg
#R$ 5,80 por Kg

#Alcatra
#R$ 5,90 por Kg
#R$ 6,80 por Kg

#Picanha
#R$ 6,90 por Kg
#R$ 7,80 por Kg

#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da
#promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no
#cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva
#um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
#fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
#pagamento, valor do desconto e valor a pagar.

carne = input("Informe qual tipo de carne quer comprar:")
carne = carne.lower()

quantidade = float(input("Informe a quantidade que deseja comprar:"))

if quantidade < 0:
    print("Valor inválido")
    exit

if carne == "file duplo":
    if quantidade <= 5:
        preco = quantidade * 4.9
    else:
        preco = quantidade * 5.8
elif carne == "alcatra":
    if quantidade <= 5:
        preco = quantidade * 5.9
    else:
        preco = quantidade * 6.8
elif carne == "picanha":
    if quantidade <= 5:
        preco = quantidade * 6.9
    else:
        preco = quantidade * 7.8
else:
    print("Opção inexistente na promoção.")

resposta = input("Tem cartao Tabajara?")
resposta = resposta.lower()

preco = round(preco, 2)

if resposta == "sim":
    valor_pagar = preco * .95
    desconto = preco - valor_pagar
    print("\nNota Fiscal\nQuantidade: Kg", quantidade,
      "\nPreço total: R$", round(preco, 2),"\nCartão Tabajara: sim\nDesconto: R$",
      round(desconto, 2),"\nValor a pagar:", round(valor_pagar, 2))
else:
    valor_pagar = preco
    desconto = preco - valor_pagar
    print("\nNota Fiscal\nQuantidade: Kg", quantidade,
          "\nPreço total: R$", round(preco, 2), "\nCartão Tabajara: não\nDesconto: R$",
          round(desconto, 2), "\nValor a pagar:", round(valor_pagar, 2))