''' 
Module servant a faire les interractions 
avec la memoire permanente de l'ordinateur
'''
import os
import pickle


nom_fichier_sauvegarde="sauvegarde_Azul"


def demande_charger_partie():
    ''' 
    demande si l'utilisateur veut charger une nouvelle partie
    '''
    print("voulez vous charger une ancienne partie ?(o/n)")
    rep=input()
    return rep=="o"

def fichier_existe():
    ''' 
    verifie si le fichier de sauvegarde existe
    '''
    if os.path.isfile(nom_fichier_sauvegarde):
        print("chargement de la sauvegarde")
        return True
    else:
        print("fichier de sauvegarde non trouvé")
        return False

def sauvegarde(nombre_joueur,liste_donnee_joueur,sac_tuile,compteur):
    ''' 
    sauvegarde le contenu du plateau
    '''
    with open(nom_fichier_sauvegarde, 'wb') as fichier: # wb pour ecrire un fichier en binaire
        pickle.dump((nombre_joueur,liste_donnee_joueur,sac_tuile,compteur), fichier)
    

def charge_donnee():
    ''' 
    charge le contenu du plateau
    '''
    with open(nom_fichier_sauvegarde, 'rb') as fichier: # rb pour lire un fichier en binaire
        return pickle.load(fichier)

def suppression_sauvegarde():
    ''' 
    supprime le fichier de sauvegarde
    (quand le jeu est fini)
    '''
    os.remove(nom_fichier_sauvegarde)
