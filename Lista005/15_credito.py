#15.A prefeitura do Rio de Janeiro abriu uma linha de crédito para seus funcionários. O valor máximo da
#prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o
#salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

print("Informe o salário bruto")
salario_bruto = float(input())
if salario_bruto < 0:
    quit()

print("Informe o valor das prestações")
valor_prestacoes = int(input())
if valor_prestacoes < 0:
    quit()

proporcao = valor_prestacoes / salario_bruto

if proporcao > 0.3:
    print("Não é possível conceder empréstimo")
else:
    print("É possível conceder empréstimo")