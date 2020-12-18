#8. entrar com o nome, nota 1 e nota 2 de um aluno, imprimir nome, Nota1, nota2, média e a mensagem
#aprovado, reprovado ou em prova final. (a média é 7 para aprovado, 3 para reprovado, e as demais para
#prova final.

print("Informe um nome:")
nome = input()

print("Informe as notas:")
nota_01 = float(input())
nota_02 = float(input())

if nota_01 or nota_02 > 10 or nota_01 or nota_02 < 0:
    print("Nota inválida")
    quit()

media = (nota_02 + nota_02) / 2

if media >= 7:
    print("Aprovado/a")
elif media <= 3:
    print("Reprovado/a")
else:
    print("Em prova final")

print("Nome:", nome)
print("Média:", media)
print("Nota 01:", nota_01)
print("Nota 02:", nota_02)
