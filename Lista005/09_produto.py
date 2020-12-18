#9.Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
#menor que 20,00, caso contrário o lucro será de 30%. entrar com o valor do produto e imprimir o valor da
#venda.

print("Informe o valor de compra do produto:")
valor_compra = float(input())

if valor_compra < 20:
    valor_venda = valor_compra * 1.45
else:
    valor_venda = valor_compra * 1.3

print("Valor de venda: R$", valor_venda)