#10. sabendo-se que somente os municípios que possuem mais de 20 mil eleitores
#aptos tem segundo turno nas eleições para prefeito caso o primeiro colocado
#não tenha mais do que 50% DOS VOTOS. FAZER UM PROGRAMA QUE LEIA O NOME do município, a
#quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se ele terá ou não
#segundo turno.

print("Informe o nome do município:")
municipio = input()
print("Informe o número de eleitores aptos:")
eleitores_aptos = int(input())
if eleitores_aptos < 0:
    quit()
print("Informe o número de votos a favor do candidato mais popular:")
votos_candidato = int(input())
if votos_candidato > eleitores_aptos:
    quit()
proporcao = float(votos_candidato / eleitores_aptos)

if eleitores_aptos > 20000:
    if proporcao > .5:
        print("Não haverá segundo turno")
    else:
        print("Haverá segundo turno")
else:
    print("Não haverá segundo turno")