
'''
Ensemble des module constituant la partie systeme (ne constituant pas une interraction directe avec l'utilisateur graphique) du jeu 

'''

from Azul_sys_avant_jeu import *
from Azul_sys_action_joueur import *
from Azul_sys_entre_manche import *
from Azul_sys_joueur_ordi import *
from Azul_sys_memoire import *


def ajout_numero_joueur(liste_donnee_joueur):
    """ 
    ajoute le numero du joueur
    """
    for i in range(len(liste_donnee_joueur)):
        liste_donnee_joueur[i]["numero_joueur"]=i+1

def affichage_joueur_gagne(liste_donnee_joueur):
    """ 
    Regarde qui est le joueur qui a gagné et affiche le classement a l'écran
    """
    ajout_numero_joueur(liste_donnee_joueur)
    liste_donnee_joueur=sorted(liste_donnee_joueur,key=lambda liste_donnee_joueur:liste_donnee_joueur["score"],reverse=True)
    texte(470, 370, "classement :",taille=15)
    for compteur,e in enumerate(liste_donnee_joueur) :
        affichage="joueur "+str(e["numero_joueur"])+ ":   "+ str(e["score"]) + " points"
        texte(470, 400+(30*compteur), affichage,taille=12)
    
