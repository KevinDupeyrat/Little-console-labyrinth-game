#! /usr/bin/python3
# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()

        # Création d'une carte, à compléter
        lab = Labyrinthe(nom_carte, contenu)
        # Ajout de la carte dans la liste de carte
        cartes.append(lab)


nombre_carte = 0
# On affiche les cartes existantes
print("Labyrinthes existants :\n")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))
    nombre_carte += 1
    # print("Le robot est aux coordonées : {} / {}".format(
    #     carte.robot[0], carte.robot[1]))
    # print("La sortie est aux coordonées : {}".format(carte.sortie))
    # print(carte)

# Si il y a une partie sauvegardée, on l'affiche, à compléter

print("\n\nParties sauvegardées :\n")
for nom_fichier in os.listdir("cartes" + os.path.sep + "sauvegardes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", "sauvegardes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()

        print("  {} - {}".format(nombre_carte + 1, nom_carte))
        # Création d'une carte, à compléter
        lab = Labyrinthe(nom_carte, contenu)
        # Ajout de la carte dans la liste de carte
        cartes.append(lab)


# Test de deplacement du roboc dans un labyrinthe
# Sans utilisateur

print("\n\nTEST DE PARTIE : \n\n")
print(cartes[1])
print("On demande au robot d'aller une fois en haut : \n")
cartes[1].robot_haut()
print("\nOn demande au robot d'aller trois fois en bas : \n")
cartes[1].robot_bas()
cartes[1].robot_bas()
cartes[1].robot_bas()
print("On demande au robot d'aller une fois en haut : \n")
cartes[1].robot_haut()
print("\nOn demande au robot d'aller une fois en gauche : \n")
cartes[1].robot_gauche()
print("\nOn demande au robot d'aller une fois en bas : \n")
cartes[1].robot_bas()
print("\nOn demande au robot d'aller une fois à droite : \n")
cartes[1].robot_droite()
cartes[1].sauvegarde()

# Test de deplacement du roboc dans un labyrinthe
# Avec utilisateur
