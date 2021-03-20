import pickle
from random import randrange
from Donnee import *


def save(save):
    with open(nom_fichier_scores, 'wb') as f:
        variable = pickle.Pickler(f)
        variable.dump(save)
        
def down_save():
    with open(nom_fichier_scores, 'rb') as f:
        mon_pickler = pickle.Unpickler(f)
        scores_joueur = mon_pickler.load()
        return scores_joueur
    
def choix_mots (liste_choix):
    mot_lettre = []
    for lettre in liste_choix[randrange(0,len(liste_choix))]:
        mot_lettre.append(lettre)
    return mot_lettre

def jeu ():
    mots = choix_mots(liste_mots)
    liste_reponce = []
    rep_while = 0
    
    print("C'est un mot de {} lettres.".format(len(mots)))
    
    #triche
    #print(mots)
    
    while rep_while < nbr_coups:
        print("Tu as {} chances pour trouver.".format(nbr_coups - rep_while))
        reponce = input("Lettre(s) à ajouter = ")
        
        if len(reponce)>1:
            for lettre in reponce:
                liste_reponce.append(lettre)

        elif len(reponce)==0:
            continue

        else:
            liste_reponce.append(reponce)
            
        if reponce in mots:
            print ("Yes")
        else:
            if len(reponce)>1:
                print("Les lettres sont ajoutées.")
            else:
                print ("No")
         
        rep = 0
        
        for lettre in mots:
            if rep != len(mots)-1:
                rep += 1

                if lettre in liste_reponce:
                    print(lettre, end = '')
                elif lettre not in liste_reponce:
                    print("?", end = '')
            else:
                if lettre in liste_reponce:
                    print(lettre)
                elif lettre not in liste_reponce:
                    print("?")
         
        rep_while += 1
        
        victoire = 0
        for lettre in mots:
            if lettre in liste_reponce:
                victoire += 1
        if victoire == len(mots):
            print("Bravo, tu as gagnié.")
            break
        
        if rep_while == nbr_coups:
            print("Tu as pardu")
            print('Le mot était "{}".'.format("".join(mots)))
                    
        
    points = nbr_coups - rep_while
    print ("Tu finis avec {} point(s).".format(points))
    
    return points
    