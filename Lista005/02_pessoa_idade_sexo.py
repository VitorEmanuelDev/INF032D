#2.Entrar como nome, idade e sexo de uma pessoa. se a pessoa for do sexo feminino e tiver menos de 25
#anos, imprimir a mensagem (ACEITA), caso contrário, imprimir NAO ACEITA

print("Informe a idade:")
idade = int(input())

print("Informe o sexo:")
sexo = input()
sexo = sexo.lower()

if sexo == 'feminino' and idade < 25:
    print("ACEITA")
else:
    print("NÃO ACEITA")