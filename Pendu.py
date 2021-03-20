import os
from Donnee import *
from Fonction import *


print("---------------START--------------")
print("Bonjour,")
nom = input("Bienvenu quel est ton nom: ")
scores = down_save()
score_fin = 0

if nom in scores:
    print("Tu as {} points.".format(scores[nom]))
else:
    print("Tu est nouveau ici {}". format(nom))
    print("donc tu commences avec 0 point.")
    scores [nom] = 0

game = True 
start = input("On commence {} ? (oui/non) ". format(nom))
if start != 'oui':
    game = False
    
rep = 1
while game:
    print("---------Partie {} ---------".format(rep))
    
    points = jeu()

    stop = input("Veux-tu faire une nouvelle partie ? (oui/non) ")
    if stop == 'non':
        game = False

    rep += 1
    score_fin += points
    
print ("Reviens quand tu veux.")
print("Tu as gagnié {} point(s), cela fait un total de {} points.".format(score_fin, scores[nom]+ score_fin))

scores[nom] = score_fin + scores[nom]
save(scores)

os.system("pause")