from random import randint
from time import sleep 
from Azul_sys_action_joueur import joueur_joue

#########################################
#l'ordinateur choisit son conteneur et  #
#le rang des contenaire                 #
#########################################
def ordinateur_choisit_contenaire_1(table,lst_fabrique):
    
    if randint(1, 2)==1 and len(table)!=0:        #prend une tuile dans la table
        return table
    else :
        return lst_fabrique

def ordinateur_choisit_rang_table(table):
    return (randint(0, len(table)-1),-1,-1)

def ordinateur_choisit_rang_fabrique(nombre_fabrique):
    return(randint(0, nombre_fabrique-1),randint(0, 1),randint(0, 1))

def ordinateur_choisit_contenaire_2(motif,plancher):
    ''' 
    returne le contenaire choisit 
    ainsi que le rang de la ligne choisit correspondant a la ligne de la mosaique
    étant donné que le plancher n'est pas associé a une des ligne de la mosaique
    alors le rang est egal a -1

    '''
    if randint(1, 6)!=1:
        rang=ordinateur_choisit_rang_motif()
        return motif[rang],rang
    else:
        return plancher

def ordinateur_choisit_rang_motif():
    return randint(0, 4)



def ordinateur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif, plancher,mosaique):
    '''
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    #l'ordinateur choisit quoi choisir
    sleep(0.5)
    while (True):
        rang1=0
        premier_contenaire=ordinateur_choisit_contenaire_1(table,lst_fabrique)
        if premier_contenaire==table:
            rang1=ordinateur_choisit_rang_table(table)
        else :
            rang1=ordinateur_choisit_rang_fabrique(len(lst_fabrique))
        second_contenaire=ordinateur_choisit_contenaire_2(motif, plancher)
            
        if type(second_contenaire) == type(tuple()): 
            #on execute se bout si le contenaire choisit est une ligne motif
            retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire[0], plancher,rang1[0],rang1[1],rang1[2],mosaique[second_contenaire[1]] ) 
            #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
        else:
            retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, plancher,rang1[0],rang1[1],rang1[2]) 
            #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
        
        if retour_joueur_joue!=False:       #si l'ordinateur a fait un coup correcte ...
            table+=retour_joueur_joue
            return compteur + 1


def ordinateur_choisit_contenaire_et_joue_solo(compteur, table, lst_fabrique, motif, plancher,mosaique):
    '''
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    #l'ordinateur choisit quoi choisir
    sleep(0.5)
    while (True):

        rang1=0
        premier_contenaire=ordinateur_choisit_contenaire_1(table,lst_fabrique)
        if premier_contenaire==table:
            rang1=ordinateur_choisit_rang_table(table)
        else :
            rang1=ordinateur_choisit_rang_fabrique(len(lst_fabrique))
        second_contenaire=ordinateur_choisit_contenaire_2(motif, plancher)
        boite=[0]*7     #l'ordinateur n'a pas de malus dans le mode solo,pour recicler le code on fait donc un plancher n'ayant aucun rapport avec celui utilisé d'habitude
        if type(second_contenaire) == type(tuple()): 
            #on execute se bout si le contenaire choisit est une ligne motif
            retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire[0], boite,rang1[0],rang1[1],rang1[2],mosaique[second_contenaire[1]] ) 
            #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
        else:
            retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, boite,rang1[0],rang1[1],rang1[2]) 
            #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
        
        if retour_joueur_joue!=False:       #si l'ordinateur a fait un coup correcte ...
            table+=retour_joueur_joue
            return compteur + 1

