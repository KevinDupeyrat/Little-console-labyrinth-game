#! /usr/bin/python3
# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from labyrinthe import Labyrinthe


def affichage_list_carte(cartes=[]):
    """ Fonction d'affichage de carte.
    Elle affiche toutes les cartes présente dans
    le dossier 'cartes' ainsi que les partie qui sont engegistrée """

    # On charge les cartes existantes
    # qui sont présentent dans le dossier 'cartes'
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-4].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()

            # Création d'une carte, à compléter
            lab = Labyrinthe(nom_carte, contenu)
            # Ajout de la carte dans la liste de carte
            cartes.append(lab)

    nombre_total_carte = 0
    # On affiche les cartes existantes
    print("\t\tLabyrinthes existants :\n")
    for i, carte in enumerate(cartes):
        print("\t\t\t{} -> {}".format(i + 1, carte.nom))
        nombre_total_carte += 1

    nombre_carte_base = len(cartes)
    i = int(nombre_carte_base)

    # Si il y a une partie sauvegardée, on l'affiche
    print("\n\n\t\tParties sauvegardées :\n")
    for nom_fichier in os.listdir("cartes" + os.path.sep + "sauvegardes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", "sauvegardes", nom_fichier)
            nom_carte = nom_fichier[:-4].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()

            print("\t\t\t{} -> {}".format(i + 1, nom_carte))
            i += 1
            # Création d'une carte, à compléter
            lab = Labyrinthe(nom_carte, contenu)
            # Ajout de la carte dans la liste de carte
            cartes.append(lab)

    return nombre_carte_base


def jouer(labyrinthe):
    """ Fonction qui s'occupe du jeu en lui même, c'est à dire
    une fois qu'on a fait le choix de la carte """

    print("C'est partie !!\n")
    partie_terminee = False
    direction = ' '

    # Tant que l'utilisateur ne gagne pas
    # Ou qu'il n'appui pas sur 'q'
    while not partie_terminee:
        nombre_fois = 1
        direction = input("--> ")

        # Vérification du nombre de caractère saisie
        while len(direction) > 2 or len(direction) == 0:
            print("Nombre de caractère incorrecte")
            direction = input("--> ")

        # Si l'utilisateur saisi 2 caractères,
        # On vérifie que le second est bien un
        # nombre
        if len(direction) == 2:
            while True:
                try:
                    nombre_fois = int(direction[1])
                    direction = direction[0].lower()

                    break
                except ValueError:
                    print("Le deuxième argument doit être un nombre")
                    direction = input("--> ")
                    if len(direction) < 2:
                        break
                    else:
                        pass
        else:
            direction = direction.lower()

        i = 0
        while i < nombre_fois:
            if direction == 'n':
                partie_terminee = labyrinthe.robot_haut()
                labyrinthe.sauvegarde()
            elif direction == 's':
                partie_terminee = labyrinthe.robot_bas()
                labyrinthe.sauvegarde()
            elif direction == 'e':
                partie_terminee = labyrinthe.robot_droite()
                labyrinthe.sauvegarde()
            elif direction == 'o':
                partie_terminee = labyrinthe.robot_gauche()
                labyrinthe.sauvegarde()
            elif direction == 'q':
                labyrinthe.sauvegarde()
                return direction
            else:
                print("Je n'ai pas compris votre réponse.")
                nombre_fois = 1
                break

            i += 1
            if partie_terminee:
                labyrinthe.supprimer_sauvegarge()
                break


def main():
    """ Fonction principale de lancement du jeu.
    Celui ci permet de faire le choix de la carte et de
    demander si on veut rejouer une partie.
    Le reste de l'applicatif est transmise à des fonction externe """

    # Affichage d'intro
    print("+--------------------------------------------------------------------------------------------------------------------------------------+")
    print("|      ___       ___           ___           ___           ___                       ___           ___           ___           ___     |")
    print("|     /\__\     /\  \         /\  \         |\__\         /\  \          ___        /\__\         /\  \         /\__\         /\  \    |")
    print("|    /:/  /    /::\  \       /::\  \        |:|  |       /::\  \        /\  \      /::|  |        \:\  \       /:/  /        /::\  \   |")
    print("|   /:/  /    /:/\:\  \     /:/\:\  \       |:|  |      /:/\:\  \       \:\  \    /:|:|  |         \:\  \     /:/__/        /:/\:\  \  |")
    print("|  /:/  /    /::\~\:\  \   /::\~\:\__\      |:|__|__   /::\~\:\  \      /::\__\  /:/|:|  |__       /::\  \   /::\  \ ___   /::\~\:\  \ |")
    print("| /:/__/    /:/\:\ \:\__\ /:/\:\ \:|__|     /::::\__\ /:/\:\ \:\__\  __/:/\/__/ /:/ |:| /\__\     /:/\:\__\ /:/\:\  /\__\ /:/\:\ \:\__\|")
    print("| \:\  \    \/__\:\/:/  / \:\~\:\/:/  /    /:/~~/~    \/_|::\/:/  / /\/:/  /    \/__|:|/:/  /    /:/  \/__/ \/__\:\/:/  / \:\~\:\ \/__/|")
    print("|  \:\  \        \::/  /   \:\ \::/  /    /:/  /         |:|::/  /  \::/__/         |:/:/  /    /:/  /           \::/  /   \:\ \:\__\  |")
    print("|   \:\  \       /:/  /     \:\/:/  /     \/__/          |:|\/__/    \:\__\         |::/  /     \/__/            /:/  /     \:\ \/__/  |")
    print("|    \:\__\     /:/  /       \::/__/                     |:|  |       \/__/         /:/  /                      /:/  /       \:\__\    |")
    print("|     \/__/     \/__/         ~~                          \|__|                     \/__/                       \/__/         \/__/    |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------+")

    print("\n\nBienvenu dans le jeu du Labyrinthe !")

    nouvelle_partie = 'y'
    while nouvelle_partie == 'y' or (nouvelle_partie != 'n' and nouvelle_partie != 'y' and nouvelle_partie != 'q'):

        if nouvelle_partie != 'n' and nouvelle_partie != 'y' and nouvelle_partie != 'q':

            print("Je n'ai pas compris votre réponse")
            print("Voullez vous refaire une partie ? y / n ")
            nouvelle_partie = input("\n--> ")
            nouvelle_partie = nouvelle_partie.lower()

        else:

            continuer = 'n'
            while continuer == 'n' or (continuer != 'n' and continuer != 'y'):

                if continuer == 'n':
                    print("\n\n  - Faite votre choix dans les différantes cartes : \n")

                    cartes = []
                    nombre_carte_base = affichage_list_carte(cartes)

                    # Vérifivation que nous entrons bien un nombre
                    while True:
                        index = input("\n\n--> ")
                        try:
                            index = int(index)

                            if index < 1 or index > len(cartes):
                                raise ValueError
                            break
                        except ValueError:
                            print("Je n'ai pas compris votre réponse")
                            pass

                    # Nous allons vérifier que la carte choisi
                    # ne correspond pas a une partie en cour
                    # sinon on l'indique à l'utilisateur
                    compteur_partie_enregiste = 0
                    for i, carte in enumerate(cartes):
                        if carte.nom == cartes[index - 1].nom:
                            compteur_partie_enregiste += 1

                    if compteur_partie_enregiste > 1:
                        print("La carte ' {} ' a déjà une partie en cours, si vous continuez elle sera écrasé.".format(
                            cartes[index - 1].nom))
                        print("Continuer ? y / n ")
                        continuer = input("\n--> ")
                        continuer = continuer.lower()
                    else:
                        continuer = 'y'
                else:
                    print("Je n'ai pas compris votre réponse")
                    print("Continuer ? y / n ")
                    continuer = input("\n--> ")
                    continuer = continuer.lower()

            print("\n\nPour jouer, vous devez déplacer le robot(X) vers la sortie(U).")
            print(
                "Pour cela, vous disposez des touche N(nord) , S(sud), E(east), O(ouest)")
            print("Vous pouvez combinez une de ces touches avec un chiffre (ex: N3 avancera le robot de 3 niveaux vers le nord)")
            print("Les parties sont enregistré automatiquement à chaque coups pour pouvoir vous laisser la possibilité de finir plus tard")
            print("Vous pouvez quitter à tout moment le jeu avec le touche Q ")

            if index > nombre_carte_base:
                print("\n\nBon retour sur la carte ' {} ' vous pouvez finir votre partie: \n\n".format(
                    cartes[index - 1].nom))
            else:
                print("\n\nVous avez choisie la carte ' {} ' : \n\n".format(
                    cartes[index - 1].nom))

            print(cartes[index - 1])

            nouvelle_partie = jouer(cartes[index - 1])

            if nouvelle_partie != 'q':
                print("Voullez vous refaire une partie ? y / n ")
                nouvelle_partie = input("\n--> ")
                nouvelle_partie = nouvelle_partie.lower()

            if nouvelle_partie == 'n' or nouvelle_partie == 'q':
                print("\nAu revoire !!  :) \n")


if __name__ == '__main__':
    main()
