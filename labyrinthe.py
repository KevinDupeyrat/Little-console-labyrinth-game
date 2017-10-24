#! /usr/bin/python3
# -*-coding:Utf-8 -*

"""
   Ce module contient la classe Labyrinthe.
   Elle permet d'initialier la grille en partant d'un
   str. On initialise également le roboc
   en trouvant ses coordonnées dans la grille
"""

import copy
import os


class Labyrinthe:

    """
        Classe représentant un labyrinthe.
        Elle aurat comme attribut les dimensions du labyrinthe,
        le nom, la position du robot et la
        position de la sortie.

        Elle inclut également toutes les méthodes
        permettant la mouvement du robot dans ce labyrinthe
    """

    def __init__(self, nom, grill):
        self.nom = nom
        self.hauteur = 1
        self.largeur = 0
        self.grille = self.__init_labyrinthe(grill)
        self.grille_intacte = copy.deepcopy(self.grille)
        self.robot = self.__init_element("X")
        self.coordone_robot_ori = self.robot
        self.sortie = self.__init_element("U")

    def __init_labyrinthe(self, grille):
        """ Méthode privée d'initialisation du labyrinthe.
            Nous allons calculer les dimensions du
            labyrinthe et également transférer le
            labyrinthe de l'etat de str à une list
            à deux dimensions pour faciliter
            les mouvements du robot """

        # On fait le calcule des dimension du labyrinthe
        for i in grille:
            if i == "\n":
                self.hauteur += 1
                self.largeur = 0
            else:
                self.largeur += 1

        # List à deux dimensions
        array = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        i, k = 0, 0
        while i < self.hauteur:
            j = 0
            while j < self.largeur:

                if grille[k] is not "\n":
                    array[i][j] = grille[k]
                    j += 1
                k += 1

            i += 1

        return array

    # Méthode privée d'initialisation du robot
    # Ou de tout autre élément au besoin (sortie, mur ...)
    def __init_element(self, element):
        """ On initilise tous les éléments passé en paramètre
            pour pouvoir connaitre leur coordonées dans le
            tableau à deux dimension """

        i = 0
        while i < self.hauteur:
            j = 0
            while j < self.largeur:

                if self.grille[i][j] == element:
                    return (i, j)
                j += 1

            i += 1

    def robot_haut(self):
        """ Méthode qui demande au robot d'aller
            d'un cran vers le haut """

        return self.__bouge_le_robot(self.robot[0] - 1, self.robot[1])

    def robot_bas(self):
        """ Méthode qui demande au robot d'aller
            d'un cran vers le bas """

        return self.__bouge_le_robot(self.robot[0] + 1, self.robot[1])

    def robot_gauche(self):
        """ Méthode qui demande au robot d'aller
            d'un cran vers la gauche """

        return self.__bouge_le_robot(self.robot[0], self.robot[1] - 1)

    def robot_droite(self):
        """ Méthode qui demande au robot d'aller
            d'un cran vers la droite """

        return self.__bouge_le_robot(self.robot[0], self.robot[1] + 1)

    def __bouge_le_robot(self, x, y):
        """ Méthode privée qui permet les mouvements du robot dans
            le labyrinthe
            On vérifie si le caractère ce situent aux coordonnées
            passé en paramètre n'est pas
            un mur 'O', si c'est n'est pas le cas,
            on positionne le robot sur ces coordonnées """

        if self.grille[x][y] == "O":
            print("AIE le mur !!!!!!")
        else:
            # self.grille[self.robot[0]][self.robot[1]] = " "
            self.grille = copy.deepcopy(self.grille_intacte)
            self.grille[self.coordone_robot_ori[0]
                        ][self.coordone_robot_ori[1]] = " "
            self.grille[x][y] = "X"

            self.robot = (x, y)

        self.__affiche_labyrinthe()

        # Si le robot est aux mêmes coordonnées que la sortie
        # alors c'est gagnée et on renvoie True
        if self.robot == self.sortie:
            print("C'est gagné !!!")
            return True

    def __affiche_labyrinthe(self):
        """ Méthode d'affichage interne du labyrinthe
            Nous avons mis cette méthode en privée car l'utilisateur
            peut déja afficher le labyrinthe avec __repr__ """

        print(repr(self))

    def sauvegarde(self):
        """ Méthode qui permet la sauvegarde du labyrinthe """

        chemin = os.path.join(
            "cartes", "sauvegardes", "{}.txt".format(self.nom))
        with open(chemin, "w") as fichier:
            fichier.write(str.strip(repr(self)))

    def supprimer_sauvegarge(self):
        """ Méthode qui permet de supprimer une sauvagerde
            quand cette partie est terminée """
        os.remove(os.path.join(
            "cartes", "sauvegardes", "{}.txt".format(self.nom)))

    def __repr__(self):
        """ Permet de renvoyer la string du labyrinthe pour l'afficher """

        i, j = 0, 0
        string = ""
        while i < self.hauteur:
            j = 0
            while j < self.largeur:
                string += self.grille[i][j]
                j += 1
            string += "\n"
            i += 1

        return string

    def __str__(self):

        return repr(self)
