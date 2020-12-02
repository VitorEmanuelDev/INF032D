#2. Entrar com quatro números e imprimir a media ponderada, sabendo-se que os pesos são respectivamente 1,2,3,4.

print("Informe as quatro notas:")
nota_01 = float(input())
nota_02 = float(input())
nota_03 = float(input())
nota_04 = float(input())

media_ponderada = (nota_01 + (nota_02 * 2) + (nota_03 * 3) + (nota_04 * 4)) / 10

print("Média ponderada:", media_ponderada)