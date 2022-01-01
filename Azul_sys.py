
'''
Ensemble des module constituant la partie systeme (ne constituant pas une interraction directe avec l'utilisateur graphique) du jeu 

'''

from Azul_sys_avant_jeu import *
from Azul_sys_action_joueur import *
from Azul_sys_entre_manche import *
from Azul_sys_joueur_ordi import *
from Azul_sys_memoire import *


def affichage_joueur_gagne(liste_donnee_joueur):
    """ 
    Regarde qui est le joueur qui a gagné et affiche
    """
    joueur_gagnant=(1,liste_donnee_joueur[0]["score"])
    for i in range(1,len(liste_donnee_joueur)):
        if joueur_gagnant[1]<liste_donnee_joueur[i]["score"]:
            joueur_gagnant=(i+1,liste_donnee_joueur[i]["score"])
    print("le joueur qui a gagné est le joueur :",joueur_gagnant[0])
