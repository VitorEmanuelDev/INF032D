#3. Utilizando o del, remova todos os elementos da lista criada anteriormentefrutas = ["Banana", "Manga", "Abacaxi", "Siriguela"]
frutas = ["Banana", "Manga", "Abacaxi", "Siriguela"]
doces = ["Brigadeiro", "cajuzinho", "Beijinho", "Casadinho"]
feijoada = ["Feijão preto","linguiça calabresa","Costela de porco","Paio"]

listona = [frutas, doces, feijoada]

print(listona[1][0])

doces.append("Brigadeiro")

print(listona)

listona.append("corote")

print(listona)

del listona[0:-1]

print(listona)