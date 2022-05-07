from itertools import combinations_with_replacement

vetor = []
possibilities = []
numero = int(input("Digite o número que se deseja alcançar com as somas."))

while True:
    v = input("Digite o número de possibilidade de soma. Para finalizar o fornecimento de informações, "
                  "dê Enter.")
    if v == "" or v == ' ':
        break
    else:
        vetor.insert(0,int(v))

bestTuple = None
bestTuple2 = None
for i in range(0,numero+1):
    combinations = list(combinations_with_replacement(vetor, i))
    for tupla in combinations:
        if sum(tupla) == numero:
            possibilities.insert(0, tupla)

for j in range(0,len(possibilities)):
    if j == 0 :
        bestTuple = possibilities[j]
    elif len(bestTuple) > len(possibilities[j]):
        bestTuple = possibilities[j]
    elif len(bestTuple) < len(possibilities[j]):
        bestTuple = bestTuple
    elif len(bestTuple) == len(possibilities[j]) and bestTuple != possibilities[j]:
        bestTuple2 = possibilities[j]
        bestTuple = bestTuple

print(bestTuple)
if bestTuple2 is not None and len(bestTuple2) == len(bestTuple):
    print(bestTuple2)
