#2. Crie três listas, uma lista de cada coisa a seguir:
#• frutas
#• docinhos de festa (não se esqueça de brigadeiros!!)
#• ingredientes de feijoada
#Lembre-se de salvá-las em alguma variável!
#a. Agora crie uma lista que contém essas três listas.
#Nessa lista de listas (vou chamar de listona):
#b. você consegue acessar o elemento brigadeiro?
#c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos
#de festa?
#d. Adicione bebidas ao final da listona, mas sem criar uma lista!

frutas = ["Banana", "Manga", "Abacaxi", "Siriguela"]
doces = ["Brigadeiro", "cajuzinho", "Beijinho", "Casadinho"]
feijoada = ["Feijão preto","linguiça calabresa","Costela de porco","Paio"]

listona = [frutas, doces, feijoada]

print(listona[1][0])

doces.append("Brigadeiro")

print(listona)

listona.append("corote")

print(listona)