import random
import doctest
import Azul
from time import sleep 


def initialisation_plancher():
    ''' 
    initialise le contenu du plancher


    >>> plancher=initialisation_plancher()
    >>> print(plancher)
    [0, 0, 0, 0, 0, 0, 0]
    '''
    return [0]*7

def initialisation_table():
    '''
    initialise le contenu de la table
    '''

    return[-1]      # -1 est le jeton pour indiquer qui commence la prochaine manche

def initialisation_mosaique():
    '''
    initialise la mosaique (n'est presque pas solicité pour la phase 1)

    retourne une matrice de 5*5


    >>> initialisation_mosaique()
    [[10, 6, 7, 8, 9], [9, 10, 6, 7, 8], [8, 9, 10, 6, 7], [7, 8, 9, 10, 6], [6, 7, 8, 9, 10]]
    '''
    ligne=[6,7,8,9,10]
    mosaique=[]
    for i in range(5):  
        derniere_val=[ligne.pop()]        
        ligne = derniere_val +ligne # retire la derniere valeur de ligne pour la mettre en premiere position
        mosaique.append(list(ligne))
    return mosaique

def initialisation_motif():
    '''
    initialise les lignes motifs
    retourne une liste de liste
    '''
    motif=[]
    for i in range(5):
        ligne=[]
        for j in range(i+1):
            ligne.append(0)
        motif.append(ligne)
    return motif

def preparation_sac_tuile():
    '''Fonction préparant le sac de tuile en début de partie
    la fonction retourne une liste contenant 100 valeur mélangés variant entre 1 et 5
    chacune apparraissant 20 fois  
    
    >>> l=[]
    >>> for i in range(20):
    ...    l.append(1)
    ...    l.append(2)
    ...    l.append(3)
    ...    l.append(4)
    ...    l.append(5)
    >>> l==preparation_sac_tuile()
    False
    >>> a=preparation_sac_tuile()
    >>> a.count(1)==20 and a.count(3)==20 and a.count(4)==20 and a.count(5)==20
    True
    >>> len(a)==100
    True
    '''
    sac_tuile=[]
    for i in range(20):
        for j in range(1,6):
            sac_tuile.append(j)
    random.shuffle(sac_tuile)   #fonction melangeant la liste donné en paramettre
    return sac_tuile

def preparation_une_usine(sac_tuile):
    '''prépare une usine en plaçant 4 tuiles dans une usine,les tuiles sont enlevé du sac de tuile
        la fonction retourne une usine (c'est a dire,une matrice de 2*2 )
    >>> a=[1, 2, 1, 1, 2, 4, 5, 6]
    >>> preparation_une_usine(a)
    [[6, 5], [4, 2]]
    >>> print (a)
    [1, 2, 1, 1]
    '''
    usine=[]
    for i in range(2):
        ligne_usine=[]
        for j in range(2):
            ligne_usine.append(sac_tuile.pop())
        usine.append(ligne_usine)
    return usine


def preparation_usines(sac_tuile,nbr_usine=5):
    '''prepare les differentes usines 
    >>> preparation_usines([2,3,5,4,1,1,1,2,3,5,6,6,8,4,5,1,2,3,5,5])
    [[[5, 5], [3, 2]], [[1, 5], [4, 8]], [[6, 6], [5, 3]], [[2, 1], [1, 1]], [[4, 5], [3, 2]]]
    '''
    lst_usine=[]
    for n in range(nbr_usine):
        lst_usine.append(preparation_une_usine(sac_tuile))
        
    return lst_usine

def demande_joueur_ordinateur():
    '''demande a l'utilisateur si les joueurs seront des "ordinateur" ou de vrai joueur  '''
    lst=[]
    for i in range(2):
        print("voulez vous que le joueur ",i+1," soit un joueur ou un ordinateur(joueur/ordinateur)")
        lst.append(str(input()))
    return lst

def fabrique_vide(lst_fabrique):
    ''' 
    verifie si les fabrique sont vide
    si vrai renvoie True sinon False
    '''
    for e in lst_fabrique:
        for colonne in e:
            for ligne in colonne:
                if ligne!=0:
                    return False
    return True

def detecte_fin_manche(lst_fabrique,table):
    ''' 
    detecte la fin de la manche en verifiant le contenu des usine et de la table
    renvoie True si lst_fabrique et table ne comporte aucune tuile
    '''
    return fabrique_vide(lst_fabrique) and not table

#########################################
#l'ordinateur choisit son conteneur et  #
#le rang des contenaire                 #
#########################################
def ordinateur_choisit_contenaire_1(table,lst_fabrique):
    
    if random.randint(1, 2)==1 and len(table)!=0:        #prend une tuile dans la table
        return table
    else :
        return lst_fabrique

def ordinateur_choisit_rang_table(table):
    return (random.randint(0, len(table)-1),-1,-1)

def ordinateur_choisit_rang_fabrique():
    return(random.randint(0, 4),random.randint(0, 1),random.randint(0, 1))

def ordinateur_choisit_contenaire_2(motif,plancher):
    if random.randint(1, 6)!=1:
        rang=ordinateur_choisit_rang_motif()
        return motif[rang]
    else:
        return plancher

def ordinateur_choisit_rang_motif():
    return random.randint(0, 4)



def ordinateur_choisit_contenaire_et_joue(compteur, table, lst_fabrique, motif, plancher):
    '''
    le joueur choisit les contenaires utilisé puis effectue l'action

    retourne le compteur(int)   celui si sert a faire jouer le prochain joueur
    '''
    
    #l'ordinateur choisit quoi choisir
    #Azul.attente_clic()
    sleep(0.5)
    while (True):
        rang1=0
        premier_contenaire=ordinateur_choisit_contenaire_1(table,lst_fabrique)
        if premier_contenaire==table:
            rang1=ordinateur_choisit_rang_table(table)
        else :
            rang1=ordinateur_choisit_rang_fabrique()
        second_contenaire=ordinateur_choisit_contenaire_2(motif, plancher)
            

        retour_joueur_joue=joueur_joue(premier_contenaire, second_contenaire, plancher,rang1[0],rang1[1],rang1[2] ) #si la fonction ne ressort pas False ,on fait jouer le joueur suivant,sinon on refait jouer le meme joueur car le coup n'est pas permis
                
        if retour_joueur_joue!=False:       #si l'ordinateur a fait un coup correcte ...
            table+=retour_joueur_joue
            return compteur + 1


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

def qui_commence(plateau_1,plateau_2):
    if -1 in plateau_1:
        return 0
    elif -1 in plateau_2:
        return 1
    else:
        return 0

def complete_ligne(ligne_plateau,valeur,nombre_a_rajouter):
    '''
    rajoute le nombre de tuiles dans la ligne,et renvoie le nombre en surplus
    
    >>> ligne=[0,0,0,0]
    >>> print( complete_ligne(ligne,5,8))
    4
    >>> print (ligne)
    [5, 5, 5, 5]
    '''
    #if nombre_a_rajouter==0:
    #           return nombre_a_rajouter
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
    for i in range(7):
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




def joueur_joue(contenaire_1,contenaire_2,plancher,n,i,j):
    '''
    fonction regroupant toute les sous fonction a faire apres que le joueur est sélection les 2 contenaire

    le premier argument est forcément une fabrique ou la table 
    n= numero de la fabrique selectionner
    i=ligne de la tuile selectionner
    j=colonne de la tuile selectionner
    retourne la liste de tuiles restante de la fabrique ou false si le coup n'est pas jouable
    '''
    
    val_tuile_select=0

    if i!=-1 :   #valeur ajouter au tuples de la table, sert a différencier la table et la fabrique
        #code a effectuer si le contenaire choisit est la fabrique
        val_tuile_select=contenaire_1[n][i][j]
        if val_tuile_select==0:
            return False            #si c'est une tuiles vide
        elif len(contenaire_2)!=7:
            if (not ligne_vide(contenaire_2) and contenaire_2.count(val_tuile_select)==0) \
                or contenaire_2.count(val_tuile_select)==len(contenaire_2): 
                return False    #il y a deja des tuiles d'une autre couleur dans la ligne motif ou le joueur veut mettre des tuiles de la meme couleurs dans une ligne remplis de cette couleur
        
        lst_autre_tuiles =valeur_differente_tuile_fabrique(contenaire_1[n], val_tuile_select)
        nbr_restant=4-len(lst_autre_tuiles)
        nbr_restant=complete_ligne(contenaire_2,val_tuile_select ,4-len(lst_autre_tuiles)) #4 etant le nombre de tuiles que contient une fabrique
        complete_plancher(plancher,val_tuile_select,nbr_restant)
        vide_fabrique(contenaire_1[n])
        

        return lst_autre_tuiles     #les met dans la table
    elif i==-1:
        val_tuile_select=contenaire_1[n]    #code a effectuer si le premier contenaire est la table
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
    
    
    
if __name__=="__main__":
    #doctest.testmod()
    Azul.main()
