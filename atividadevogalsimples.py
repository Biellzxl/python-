#vogal simplificado


vetor = []

for i in range (10):
    consoante = input("digite uma letra de a - z: ")
    if consoante not in ["a","e", "i", "o", "u"]:
        vetor.append(consoante)

print("o vetor possui ", len(vetor), "posicoes de constantes lidas")
print("consoantes digitas: ", vetor)