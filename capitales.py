import sys, random

# input a number
nombreQuestion = int(sys.argv[1])
chercheC = sys.argv[2]

country = []
capitale = []
fd = open("./capitales.csv", "r")
for ligne in fd.readlines() :
    cc = ligne.split(",")
    country.append(cc[0])
    capitale.append(cc[1][:-1])

for i, c in enumerate(capitale) :
    if c == chercheC :
        print("Pays qui a la capitale ", chercheC, " est : ", country[i])
        break
else :
    print("can't find country for this capital")

i=0
bonneReponse=0
while i < nombreQuestion :
    index = random.randint(0, len(country)-1)
    print(country[index])
    inputC = input("Capitale ?")
    if (country[index]=="Israël") :
        if (inputC == "None" or inputC == "none" or inputC == "" or inputC == " " or inputC == " -" or inputC == "-") :
            bonneReponse+=1
            print("Bravo!")
        else :
            print("pas de capitale")
    else :
        if (inputC == capitale[index]) :
            bonneReponse+=1
            print("Bravo!")
        else :
            print("la bonne reponse est : ", capitale[index])
    del country[index]
    del capitale[index]
    i+=1
print("le nombre de bonne reponse est : ", bonneReponse,"\nle pourcentage de bonnes reponses est : ", "{:.2%}".format(bonneReponse/nombreQuestion))