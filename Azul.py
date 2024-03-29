#!/bin/python3 
from Azul_graph import *
from Azul_sys import *
#remarque :
#Pour annuler le premier element choisit,il suffit de cliquer autre part pour le deselectionner


def main():
    
    #initialisation
    donnee_joueur= menu_selection()
    if type(donnee_joueur) is type(None) :    #charge la sauvegarde
        nombre_joueur,liste_donnee_joueur,sac_tuile,compteur= charge_donnee()
    else:
        
        nombre_joueur=len(donnee_joueur)
        liste_donnee_joueur=initialisation_donnees_joueurs(donnee_joueur)
        
        sac_tuile=preparation_sac_tuile()
        compteur=0
    #fin initialisation

    cree_fenetre(1200,1000)
    
    while not condition_fin(sac_tuile,liste_donnee_joueur,nombre_joueur):
        table=initialisation_table()

        lst_fabrique=preparation_usines(sac_tuile,nombre_joueur)
        dessine_plateau(lst_fabrique,table,liste_donnee_joueur)
        while not detecte_fin_manche(lst_fabrique, table):
            joueur=compteur%len(liste_donnee_joueur)
            compte_point_tout_joueur(liste_donnee_joueur)
            dessine_plateau(lst_fabrique, table, liste_donnee_joueur)
            if nombre_joueur==1:    #variante solo du jeu 
                if liste_donnee_joueur[joueur]['type_joueur']=="j":
                    compteur=joueur_choisit_contenaire_et_joue_solo(compteur, table, lst_fabrique,\
                                                                liste_donnee_joueur[joueur]['mosaique'],\
                                                                liste_donnee_joueur[joueur]['motif'],\
                                                                liste_donnee_joueur[joueur]['coord_motif'],\
                                                                liste_donnee_joueur[joueur]['plancher'],\
                                                                liste_donnee_joueur[joueur]['coord_plancher'])
                else :
                    compteur=ordinateur_choisit_contenaire_et_joue_solo(compteur, table, lst_fabrique,\
                                                                    liste_donnee_joueur[joueur]['motif'],\
                                                                    liste_donnee_joueur[joueur]['mosaique'])
            else:
                if liste_donnee_joueur[joueur]['type_joueur']=="j":
                    compteur=joueur_choisit_contenaire_et_joue(compteur, table, lst_fabrique,\
                                                                liste_donnee_joueur[joueur]['mosaique'],\
                                                                liste_donnee_joueur[joueur]['motif'],\
                                                                liste_donnee_joueur[joueur]['coord_motif'],\
                                                                liste_donnee_joueur[joueur]['plancher'],\
                                                                liste_donnee_joueur[joueur]['coord_plancher'])
                else :
                    compteur=ordinateur_choisit_contenaire_et_joue(compteur, table, lst_fabrique,\
                                                                    liste_donnee_joueur[joueur]['motif'],\
                                                                    liste_donnee_joueur[joueur]['plancher'],\
                                                                    liste_donnee_joueur[joueur]['mosaique'])
        if nombre_joueur==1:
            compteur=1          #dans la variante solo,l'ordinateur commence toujours
        else:
            compteur = qui_commence(liste_donnee_joueur)
        action_fin_manche(liste_donnee_joueur,sac_tuile,lst_fabrique)
        dessine_plateau(lst_fabrique,table,liste_donnee_joueur)
        sauvegarde(nombre_joueur,liste_donnee_joueur,sac_tuile,compteur)
    affichage_joueur_gagne(liste_donnee_joueur)
    mise_a_jour()
    #suppression_sauvegarde()
    attente_clic()
    ferme_fenetre()



if __name__ == '__main__':

    main()
