from upemtk import *
from math import sqrt




def couleur_tuiles(tuile): #chaque fonction dessins utilise cette fonctions pour colorer les tuiles 
    '''
    compare la valeur de la tuile avec les valeurs valeur si dessous
    renvoie la couleur a la quelle la tuile correspond
    lance une exception si la valeur de la tuile n'est pas correcte
    '''
    lst_couleurs=["white","red","blue","orange","green","black","red2","blue2","orange2","green2","grey9"]
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
def dessine_plateau(mosaique_1,mosaique_2,plancher_1,plancher_2,motif_1,motif_2,lst_fabrique,table):
    dessine_fond()
    
    dessine_mosaique(mosaique_1,250,120)  #il faut garder un ecart de 40 entre A et B  et  C et D 
    dessine_mosaique(mosaique_2,950,120)

    dessine_fabrique(lst_fabrique,100,0)
    dessine_table(table, 100, 450)

    dessine_plancher(plancher_1,100,380)  #il faut garder un ecart de 50 entre A et B  et  C et D
    dessine_plancher(plancher_2,800,380)

    dessine_motif(motif_1,200,120)      
    dessine_motif(motif_2,900,120)

    mise_a_jour()

def dessine_fond():
    rectangle(0, 0, 1200, 600,"","grey")
    
def dessine_une_fabrique(fabrique,ax,ay,n):
    bx=ax+40
    by=ay+40
    a=ax    #valeur memoire pour revenir a la ligne
    b=bx    #valeur memoire pour revenir a la ligne    
    
    for i in range(2):
        ay=ay+40
        by=by+40
        for e in range(2):
            if e==0 and i==0:
                cercle(bx, by, sqrt(((bx-ax)**2)*2))
            rectangle(ax,ay,bx,by,"black",couleur_tuiles(fabrique[n][i][e])) 
            ax=ax+40
            bx=bx+40
        ax=a
        bx=b
    

def dessine_fabrique(fabrique,ax,ay):
    decalage=170
    
    for i in range(len(fabrique)):      
        dessine_une_fabrique(fabrique, ax+decalage*(i+1), ay,i)
    

def dessine_mosaique(mosaique,ax,ay):
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
        
def dessine_motif(motif,ax,ay):
    ''' 
    dessine les lignes motif
    ax et ay designe le coins haut gauche de la tuile la plus haute 
    
    '''
    bx=ax+40
    by=ay+40
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
    bx=ax+40
    by=ay+40
    a=ax    #valeur memoire pour revenir a la ligne
    b=bx    #valeur memoire pour revenir a la ligne    
    position_souris=-1
    for i in range(2):
        ay=ay+40
        by=by+40
        for e in range(2):
            if ax<coordonne[0] and coordonne[0]<bx and ay<coordonne[1] and coordonne[1]<by:
                position_souris= (n,i,e)
                rectangle(ax,ay,bx,by,"white",couleur_tuiles(fabrique[i][e]))
                
            ax=ax+40
            bx=bx+40
        ax=a
        bx=b
    return position_souris
    

def detecte_co_souris_fabrique(fabrique,ax,ay,coordonne):
    '''
    Renvoie la cases touché par la souris ou 0
    
    '''
    decalage=170
    pos_souris=-1
    
    for i in range(len(fabrique)):      # !!!
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

if __name__ == '__main__':
    pass
