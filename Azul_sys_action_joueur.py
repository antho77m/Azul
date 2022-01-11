

from Azul_graph import *
from Azul_sys_entre_manche import fabrique_vide

def complete_ligne(ligne_plateau,valeur,nombre_a_rajouter):
    '''
    rajoute le nombre de tuiles dans la ligne,et renvoie le nombre en surplus
    
    >>> ligne=[0,0,0,0]
    >>> print( complete_ligne(ligne,5,8))
    4
    >>> print (ligne)
    [5, 5, 5, 5]
    '''
    for i in range(len(ligne_plateau)):
        if ligne_plateau[i]==0:
            ligne_plateau[i]=valeur
            nombre_a_rajouter-=1
        if nombre_a_rajouter<=0:
            break
            
    return nombre_a_rajouter

def complete_plancher(plancher,valeur,nombre_a_rajouter):
    '''
    rajoute les tuiles au plancher
    
    >>> plancher=[2,3,4,5,5,5,5]
    >>> complete_plancher(plancher,7,3)
    >>> print (plancher)
    [2, 3, 4, 5, 5, 5, 5]
    >>> plancher_2=[2,2 ,0,0,0,0,0]
    >>> complete_plancher(plancher_2,3,2)
    >>> print(plancher_2)
    [2, 2, 3, 3, 0, 0, 0]
    '''
    nombre_rajouter=0
    for i in range(len(plancher)):
        if nombre_a_rajouter==nombre_rajouter:
            break
        if plancher[i]==0:
            plancher[i]=valeur
            nombre_rajouter+=1

def vide_fabrique(fabrique):
    '''
    >>> fabrique=[[0,2],[1,3]]
    >>> vide_fabrique(fabrique)
    >>> print(fabrique)
    [[0, 0], [0, 0]]
    
    '''
    for i in range(2):
        for j in range(2):
            fabrique[i][j]=0
        
def ligne_vide(ligne):
    ''' 
    verifie si la ligne donné est vide , c'est a dire qu'il y a que des valeur egal a 0
    '''
    for e in ligne:
        if e!=0:
            return False
    return True

def supprime_toute_val_contenaire(contenaire,val):
    ''' 
    supprime toute les valeurs renseigné dans les parametre,dans le contenaire
    '''
    for i in range(contenaire.count(val)):
        contenaire.remove(val)


def valeur_differente_tuile_fabrique(fabrique,valeur):
    ''' 
    renvoie les tuiles autre que valeur 
    
    >>> print(valeur_differente_tuile_fabrique([[6, 5], [4, 2]],2))
    [6, 5, 4]
    '''
    lst=[]
    for colonne in fabrique:
        for ligne in colonne:
            if ligne!=valeur:
                lst.append(ligne)
    return lst


def joueur_joue(contenaire_1,contenaire_2,plancher,n,i,j,ligne_mosaique=[]):
    '''
    fonction regroupant toute les sous fonction a faire apres que le joueur est sélectionner les 2 contenaires

    le premier argument est soit une fabrique ou la table
    tandis que le second est soit une ligne motif ou le plancher
    n= numero de la fabrique selectionner
    i=ligne de la tuile selectionner
    j=colonne de la tuile selectionner
    retourne la liste de tuiles restante de la fabrique ou false si le coup n'est pas jouable
    '''
    
    val_tuile_select=0

    if i!=-1 :   #valeur ajouter au tuples de la table, sert a différencier la table et la fabrique
        #code a effectuer si le contenaire choisit est la fabrique
        val_tuile_select=contenaire_1[n][i][j]
        if val_tuile_select==0 or val_tuile_select in ligne_mosaique:
            return False            #si c'est une tuiles vide
        elif len(contenaire_2)!=7: 
            if (not ligne_vide(contenaire_2) and contenaire_2.count(val_tuile_select)==0) \
                or contenaire_2.count(val_tuile_select)==len(contenaire_2) : 
                return False    #il y a deja des tuiles d'une autre couleur dans la ligne motif ou le joueur 
                                #veut mettre des tuiles de la meme couleurs dans une ligne remplis de cette couleur
                                #ou le joueur essaie de remplir une ligne avec une couleur deja remplie dans la mosaique
            
        
        lst_autre_tuiles =valeur_differente_tuile_fabrique(contenaire_1[n], val_tuile_select)
        nbr_restant=4-len(lst_autre_tuiles)
        nbr_restant=complete_ligne(contenaire_2,val_tuile_select ,4-len(lst_autre_tuiles)) #4 etant le nombre de tuiles que contient une fabrique
        complete_plancher(plancher,val_tuile_select,nbr_restant)
        vide_fabrique(contenaire_1[n])
        

        return lst_autre_tuiles     #les met dans la table
    elif i==-1:
        val_tuile_select=contenaire_1[n]    #code a effectuer si le premier contenaire est la table
        if val_tuile_select in ligne_mosaique:
            return False
        if len(contenaire_2)!=7:
            if (not ligne_vide(contenaire_2) and contenaire_2.count(val_tuile_select)==0) \
                or (val_tuile_select==-1 and len(contenaire_2)!=7) or contenaire_2.count(val_tuile_select)==len(contenaire_2)\
                or val_tuile_select==0:
                return False    #il y a deja des tuiles d'une autre couleur dans la ligne motif ou le joueur essaye de placer la tuiles qui permet de commencer la prochaine manche en premier
                                #dans les lignes motif ou le joueur veut mettre des tuiles de la meme couleurs dans une ligne remplis de cette couleur
        if -1 in contenaire_1:     #le premier joueur a prendre sur la table,prend le pion pour commencer la prochaine manche
            complete_plancher(plancher, -1, 1)  
            supprime_toute_val_contenaire(contenaire_1,-1)
        nbr_restant=complete_ligne(contenaire_2, val_tuile_select, contenaire_1.count(val_tuile_select))
        complete_plancher(plancher, val_tuile_select, nbr_restant)
        supprime_toute_val_contenaire(contenaire_1,val_tuile_select)
        
        return []    
    return False


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
            a=detecte_co_souris_table(table, 300, 450, coordonne_souris)
            b=detecte_co_souris_fabrique(lst_fabrique,0,0,coordonne_souris)
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

def joueur_choisit_contenaire_et_joue_solo(compteur,table,lst_fabrique,mosaique,motif,coord_motif,plancher,coord_plancher):
    '''
    fonction effectuer pour la variante solo
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    while True:         #le joueur choisit quoi choisir
        
        premier_contenaire=0
        rang1=0
        premier_choix=False
        while not premier_choix :
            coordonne_souris=attente_clic()
            a=-1
            if fabrique_vide(lst_fabrique):
                a=detecte_co_souris_table(table, 300, 450, coordonne_souris)
            b=detecte_co_souris_fabrique(lst_fabrique,0,0,coordonne_souris)
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
