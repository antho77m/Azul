#!/bin/python3 #test ...
from Azul_graph import *
from Azul_sys import *

#remarque :
#le jeton pour savoir qui commence la nouvelle manche est couleur argent
#Pour annuler le premier element choisit,il suffit de cliquer autre part pour le deselectionner
#si l'utilisateur n'écrit pas bien joueur au début alors,il sera considéré comme un ordinateur

def joueur_choisit_contenaire_et_joue(compteur,table,lst_fabrique,motif,ax_motif,ay_motif,plancher,ax_plancher,ay_plancher):
    '''
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    while True:         #le joueur choisit quoi choisir
        
        premier_contenaire=0
        rang1=0
        premier_choix=False
        while not premier_choix :
            coordonne=attente_clic()
            a=detecte_co_souris_table(table, 100, 450, coordonne)
            b=detecte_co_souris_fabrique(lst_fabrique,100,0,coordonne)
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
        coordonne=attente_clic()
        a=detecte_co_souris_motif(ax_motif,ay_motif,coordonne)
        b=detecte_co_souris_plancher(ax_plancher,ay_plancher,coordonne)
        if a !=-1:                   #le joueur a toucher la ligne motif
            second_contenaire=motif[a]
            rang2=a
            break       #le joueur a fait tout ses choix
        elif b!=-1:                  #le joueur a toucher le plancher
            second_contenaire=plancher
            break        #le joueur a fait tout ses choix
        dessine_plateau(mosaique_1, mosaique_2, plancher_1, plancher_2, motif_1, motif_2, lst_fabrique,table)


    retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, plancher,rang1[0],rang1[1],rang1[2] ) #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
    
    if retour_joueur_joue!=False:       #si le joueur a fait un coup correcte ...
        table+=retour_joueur_joue
        compteur+=1
    return compteur

def main():
    
    #initialisation
    mosaique_1=initialisation_mosaique()
    mosaique_2=initialisation_mosaique()

    sac_tuile=preparation_sac_tuile()

    plancher_1=[]
    plancher_2=[]


    lst_joueur=demande_joueur_ordinateur()  #selection joueur

    #fin initialisation
    #debut premier dessinage
    cree_fenetre(1200,600)

    #fin dessinage




    while sac_tuile:
            #initialisation des variables

        compteur = qui_commence(plancher_1,plancher_2)
        
        plancher_1=initialisation_plancher()
        plancher_2=initialisation_plancher()

        motif_1=initialisation_motif()
        motif_2=initialisation_motif()

        table=initialisation_table()

        lst_fabrique=preparation_usines(sac_tuile)

        

        dessine_plateau(mosaique_1, mosaique_2, plancher_1, plancher_2, motif_1, motif_2, lst_fabrique,table)


        while not detecte_fin_manche(lst_fabrique, table):
            
            if compteur%2==0:
                if lst_joueur[0]=="joueur":
                    compteur=joueur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif_1, 200, 120, plancher_1, 100, 380)
                else :
                        compteur=ordinateur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif_1,plancher_1 )
                    


            elif compteur%2==1:
                if lst_joueur[1]=="joueur":
                    compteur=joueur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif_2, 900, 120, plancher_2, 800, 380)
                else :
                    compteur=ordinateur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif_2, plancher_2)
                    
            dessine_plateau(mosaique_1, mosaique_2, plancher_1, plancher_2, motif_1, motif_2, lst_fabrique,table)
                

    attente_clic()
    ferme_fenetre()



if __name__ == '__main__':

    main()
