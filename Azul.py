#!/bin/python3 #juste un test
from Azul_graph import *
from Azul_sys import *
#remarque :
#le jeton pour savoir qui commence la nouvelle manche est couleur argent
#Pour annuler le premier element choisit,il suffit de cliquer autre part pour le deselectionner

def joueur_choisit_contenaire_et_joue(compteur,table,lst_fabrique,mosaique,motif,coord_motif,plancher,coord_plancher):
    '''
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    while True:         #le joueur choisit quoi choisir
        
        premier_contenaire=0
        rang1=0
        premier_choix=False
        while not premier_choix :
            coordonne_souris=attente_clic()
            a=detecte_co_souris_table(table, 100, 450, coordonne_souris)
            b=detecte_co_souris_fabrique(lst_fabrique,100,0,coordonne_souris)
            if a!=-1:
                premier_contenaire=table
                rang1=a
                premier_choix=True
            if b!=-1:
                premier_contenaire=lst_fabrique
                rang1=b
                premier_choix=True
                
        
        second_contenaire=0
        rang2=0
        coordonne_souris=attente_clic()
        a=detecte_co_souris_motif(coord_motif[0],coord_motif[1],coordonne_souris)
        b=detecte_co_souris_plancher(coord_plancher[0],coord_plancher[1],coordonne_souris)
        if a !=-1:                   #le joueur a toucher la ligne motif
            second_contenaire=motif[a]
            rang2=a
            break       #le joueur a fait tout ses choix
        elif b!=-1:                  #le joueur a toucher le plancher
            second_contenaire=plancher
            break        #le joueur a fait tout ses choix
        dessine_fabrique_et_table(lst_fabrique, table)
    if len(second_contenaire)!=7:
        retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, plancher,rang1[0],rang1[1],rang1[2],mosaique[a] ) 
        #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
    else:
        retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, plancher,rang1[0],rang1[1],rang1[2] ) 
        #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
    
    if retour_joueur_joue!=False:       #si le joueur a fait un coup correcte ...
        table+=retour_joueur_joue
        compteur+=1
    return compteur

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
