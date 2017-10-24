#! /usr/bin/python3
# -*-coding:Utf-8 -*

"""
   Ce module contient la classe Robot.
   Elle permet d'initialier le robot avec ses coordonnées
"""

class Robot:

    """Classe représentant un robot."""

    symbole = "X"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Robot x={} y={}>".format(self.x, self.y)

    def __str__(self):
        return "Robot {}.{}".format(self.x, self.y)
