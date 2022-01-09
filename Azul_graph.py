from upemtk import *
from math import sqrt
from fenetre_menu import *



def couleur_tuiles(tuile): #chaque fonction dessins utilise cette fonctions pour colorer les tuiles 
    '''
    compare la valeur de la tuile avec les valeurs valeur si dessous
    renvoie la couleur a la quelle la tuile correspond
    lance une exception si la valeur de la tuile n'est pas correcte
    '''
    #               Blanc,rouge,bleu,orange,vert,noir                      
    lst_couleurs=["#FFFFFF","#F00020","#0080FF","#FF7F00","#00561B","#000000",\
                    #les suivante sont les meme couleur en plus clair
                    "#FFB6C1","#ADD8E6","#DD7B40","#90EE90","#CECECE"]
    for i in range(len(lst_couleurs)):
        if i==tuile:
            return lst_couleurs[i]
        elif tuile==-1:
            return "silver"
    assert (False and "la valeur de la tuile est incorrect")




############################################
# Dessine les element indiquer             #
# ax et ay designe le coin haut gauche     #
# de chaque element (sauf les ligne motif) #
############################################
def dessine_plateau(lst_fabrique,table,liste_donnee_joueur):
    ''' 
    dessine le plateau
    '''
    dessine_fond()

    dessine_fabrique_et_table(lst_fabrique, table)

    for i in range(len(liste_donnee_joueur)):
        dessine_plancher(liste_donnee_joueur[i]['plancher'],\
            liste_donnee_joueur[i]['coord_plancher'][0],liste_donnee_joueur[i]['coord_plancher'][1])
        
        dessine_mosaique(liste_donnee_joueur[i]['mosaique'],\
            liste_donnee_joueur[i]['coord_mosaique'][0],liste_donnee_joueur[i]['coord_mosaique'][1])
        
        dessine_motif_et_score(liste_donnee_joueur[i]['motif'],\
            liste_donnee_joueur[i]['coord_motif'][0],liste_donnee_joueur[i]['coord_motif'][1],\
            liste_donnee_joueur[i]['score'])


    mise_a_jour()

def dessine_fabrique_et_table(lst_fabrique,table):
    ''' 
    dessine la fabrique et la table (les tuiles au centre )
    '''
    dessine_fabrique(lst_fabrique,0,0)
    dessine_table(table, 300, 450)

def dessine_fond():
    ''' 
    dessine un fond gris
    '''
    rectangle(0, 0, 1200, 1000,"","grey")
    
def dessine_une_fabrique(fabrique,ax,ay,n):
    '''
    dessine une fabrique
    '''
    bx=ax+30
    by=ay+30
    a=ax    #valeur memoire pour revenir a la ligne
    b=bx    #valeur memoire pour revenir a la ligne    
    
    for i in range(2):
        ay=ay+30
        by=by+30
        for e in range(2):
            if e==0 and i==0:
                cercle(bx, by, sqrt(((bx-ax)**2)*2))
            rectangle(ax,ay,bx,by,"black",couleur_tuiles(fabrique[n][i][e])) 
            ax=ax+30
            bx=bx+30
        ax=a
        bx=b
    

def dessine_fabrique(fabrique,ax,ay):
    ''' 
    dessine le nombre de fabrique qu'il faut
    '''
    decalage=110
    
    for i in range(len(fabrique)):      
        dessine_une_fabrique(fabrique, ax+decalage*(i+1), ay,i)
    

def dessine_mosaique(mosaique,ax,ay):
    ''' 
    dessine la mosaique (l'endroit qui est a droite des lignes motif)
    '''
    bx=ax+40
    by=ay+40
    a=ax    #valeur memoire pour revenir a la ligne
    b=bx    #valeur memoire pour revenir a la ligne 
    
    for i in range(5):
        ay=ay+40
        by=by+40
        for e in range(5):
            rectangle(ax,ay,bx,by,"black",couleur_tuiles(mosaique[i][e]) )
            
            ax=ax+40
            bx=bx+40
        ax=a
        bx=b
    
def dessine_table(table,ax,ay):
    ''' 
    dessine les tuiles sur la table (le centre du plateau)
    '''
    bx=ax+40
    by=ay+40
    a=ax        #memoire pour revenir a la ligne
    b=bx        
    for i in range(len(table)):
        
        if ax>1100:
            ax=a
            bx=b
            ay+=40
            by+=40

        rectangle(ax,ay,bx,by,"black",couleur_tuiles(table[i]))
        ax=ax+40
        bx=bx+40
        
def dessine_score_joueur(xa,ya,score,):
    ''' 
    dessine le score du joueur
    '''
    sj="score : " + str(score)
    texte(xa,ya,sj,taille=12)

def dessine_motif_et_score(motif,ax,ay,score):
    ''' 
    dessine les lignes motif 
    ax et ay designe le coins haut gauche de la tuile la plus haute 
    
    '''
    bx=ax+40
    by=ay+40
    
    dessine_score_joueur(ax-150,ay+40,score)

    a=ax    #memoire pour revenir a la ligne
    b=bx    #memoire pour revenir a la ligne
    

    for i in range(5):
        ay=ay+40
        by=by+40
        for e in range(i+1):
            rectangle(ax,ay,bx,by,"black",couleur_tuiles(motif[i][e]))
            ax=ax-40
            bx=bx-40
        ax=a
        bx=b

def dessine_plancher(plancher,ax,ay):
    ''' 
    dessine le plancher
    '''
    bx=ax+50
    by=ay+50
    for i in range(7):
        rectangle(ax,ay,bx,by,"black",couleur_tuiles(plancher[i]))
        ax=ax+50
        bx=bx+50

#################################################
#Fonction servant a recuperer l'endroit         #
#ou l'utilisateur clique                        #
#Si l'utilisateur n'a pas cliqué sur l'element  #
#verifier,la valeur retourné est -1             #
#sinon la valeur est un tuple                   #
#################################################
def detecte_co_souris_une_fabrique(fabrique,ax,ay,n,coordonne):
    bx=ax+30
    by=ay+30
    a=ax    #valeur memoire pour revenir a la ligne
    b=bx    #valeur memoire pour revenir a la ligne    
    position_souris=-1
    for i in range(2):
        ay=ay+30
        by=by+30
        for e in range(2):
            if ax<coordonne[0] and coordonne[0]<bx and ay<coordonne[1] and coordonne[1]<by:
                position_souris= (n,i,e)
                rectangle(ax,ay,bx,by,"white",couleur_tuiles(fabrique[i][e]))
                
            ax=ax+30
            bx=bx+30
        ax=a
        bx=b
    return position_souris
    

def detecte_co_souris_fabrique(fabrique,ax,ay,coordonne):
    '''
    Renvoie la cases touché par la souris ou 0
    
    '''
    decalage=110
    pos_souris=-1
    
    for i in range(len(fabrique)):      
        a=detecte_co_souris_une_fabrique(fabrique[i],ax+decalage*(i+1), ay,i,coordonne)
        if a!=-1 :
            pos_souris=a
            
    return pos_souris

def detecte_co_souris_table(table,ax,ay,coordonne):
    bx=ax+40
    by=ay+40
    a=ax        #memoire pour revenir a la ligne
    b=bx  
    position_souris=-1      
    for i in range(len(table)):
        if ax<coordonne[0] and coordonne[0]<bx and ay<coordonne[1] and coordonne[1]<by:
                position_souris= (i,-1,-1)
                rectangle(ax,ay,bx,by,"white",couleur_tuiles(table[i]))
                
        if ax>1100:
            ax=a
            bx=b
            ay+=40
            by+=40
        ax=ax+40
        bx=bx+40
    return position_souris



def detecte_co_souris_motif(ax,ay,coordonne=(0,0)):
    bx=ax+40
    by=ay+40
    a=ax    #memoire pour revenir a la ligne
    b=bx    #memoire pour revenir a la ligne
    position_souris=-1
    for i in range(5):
        ay=ay+40
        by=by+40
        
        for e in range(i+1):
            if ax<coordonne[0] and bx>coordonne[0] and coordonne[1]>ay and coordonne[1]<by:
                position_souris= i
                
            ax=ax-40
            bx=bx-40
        ax=a
        bx=b
    
    return position_souris

    
def detecte_co_souris_plancher(ax,ay,coordonne):
    bx=ax+50
    by=ay+50
    position_souris=-1
    for i in range(7):
        if ax<coordonne[0] and coordonne[0]<bx and ay<coordonne[1] and coordonne[1]<by:
                position_souris= (i)
        ax=ax+50
        bx=bx+50
    return position_souris

# affichage fin de jeu
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
    





if __name__ == '__main__':
    pass
