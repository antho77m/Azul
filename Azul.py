#!/bin/python3 
from Azul_graph import *
from Azul_sys import *
#remarque :
#Pour annuler le premier element choisit,il suffit de cliquer autre part pour le deselectionner

def main():
    
    #initialisation
    nombre_joueur=demande_nombre_joueur()

    liste_donnee_joueur=initialisation_donnees_joueurs(nombre_joueur)

    sac_tuile=preparation_sac_tuile()
    compteur=0
    #fin initialisation
    #debut premier dessinage
    cree_fenetre(1200,1000)

    #fin dessinage
    
    while sac_tuile:
        table=initialisation_table()

        lst_fabrique=preparation_usines(sac_tuile)
        dessine_plateau(lst_fabrique,table,liste_donnee_joueur)

        while not detecte_fin_manche(lst_fabrique, table):
            joueur=compteur%nombre_joueur
            compte_point_tout_joueur(liste_donnee_joueur)
            dessine_plateau(lst_fabrique, table, liste_donnee_joueur)
            
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
        compteur = qui_commence(liste_donnee_joueur)
        action_fin_manche(liste_donnee_joueur)
        dessine_plateau(lst_fabrique,table,liste_donnee_joueur)

    attente_clic()
    ferme_fenetre()



if __name__ == '__main__':

    main()
