import os, random
os.system("clear") # pour Windows : os.system("cls")

pays = []
capitales = []
fd = open("capitales.csv", "r", encoding="utf8")
for ligne in fd :
    pays.append(ligne.split(",")[0])
    capitales.append(ligne.split(",")[1][:-1])

nb = int(input("Nombre de questions : "))
numeroQuestion = 0
score = 0
while numeroQuestion < nb :
    numPays = random.randint(0, len(pays)-1)
    print("Question", numeroQuestion+1, ": capitale ", pays[numPays], ": ", end="")
    numeroQuestion += 1
    reponse = input("")
    if reponse == capitales[numPays] :
        print("Bravo !")
        score += 1
    else :
        print("La bonne réponse est ", capitales[numPays])
    del pays[numPays]
    del capitales[numPays]

print("Votre score est ", score)
