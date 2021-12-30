from random import shuffle
''' 
module repertoriant la majorité des fonctions utilisé avant le lancement de la partie 
'''


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
    shuffle(sac_tuile)   #fonction melangeant la liste donné en paramettre
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
            if sac_tuile:
                ligne_usine.append(sac_tuile.pop())
            else:
                ligne_usine.append(0)
        usine.append(ligne_usine)
    return usine


def preparation_usines(sac_tuile,nombre_joueur):
    '''prepare les differentes usines 
    >>> preparation_usines([2,3,5,4,1,1,1,2,3,5,6,6,8,4,5,1,2,3,5,5])
    [[[5, 5], [3, 2]], [[1, 5], [4, 8]], [[6, 6], [5, 3]], [[2, 1], [1, 1]], [[4, 5], [3, 2]]]
    '''
    lst_nombre_usine=[5,5,7,9]
    nbr_usine=lst_nombre_usine[nombre_joueur-1]
    lst_usine=[]
    for n in range(nbr_usine):
        lst_usine.append(preparation_une_usine(sac_tuile))
        
    return lst_usine

def demande_joueur_ordinateur(numero_joueur):
    '''demande a l'utilisateur si les joueurs seront des "ordinateur" ou de vrai joueur  '''
    while True :
        print("voulez vous que le joueur ",numero_joueur," soit un joueur ou un ordinateur(j/o)")
        type_joueur=input()
        if type_joueur=="j" or type_joueur=="o":
            return type_joueur
        print("veuillez mettre une reponse correcte")


def demande_nombre_joueur():
    print("combien de joueur voulez vous dans la partie ?")
    
    return int(input())

def initialisation_donnees_joueurs(nombre_joueur):
    ''' 
    initialise et regroupe les différente données des joueurs.
    retourne une liste de dictionnaire,un dictionnaire regroupe
    toute les information d'un seul joueur
    '''
    if nombre_joueur==1:
        nombre_joueur+=1
        variante_solo=True
    lst_coord_plancher=[(100,380),(800,380),(100,720),(800,720)]
    lst_coord_mosaique=[(250,120),(950,120),(250,460),(950,460)]
    lst_coord_motif=[(200,120),(900,120),(200,460),(900,460)]       #liste des coordonné a utilisé pour les fonction dessin,selon les joueur

    lst_donnee_joueur=[]
    for i in range(nombre_joueur):
        donnee_joueur=dict()
        donnee_joueur['coord_plancher']=lst_coord_plancher[i]
        donnee_joueur['coord_mosaique']=lst_coord_mosaique[i]
        donnee_joueur['coord_motif']=lst_coord_motif[i]
        donnee_joueur['plancher']=initialisation_plancher()
        donnee_joueur['motif']=initialisation_motif()
        donnee_joueur['mosaique']=initialisation_mosaique()
        donnee_joueur['mosaique_manche_pre']=initialisation_mosaique()
        if variante_solo and i==0:
            donnee_joueur['type_joueur']=demande_joueur_ordinateur(i+1)
        elif variante_solo:
            donnee_joueur['type_joueur']="o"
        else:
            donnee_joueur['type_joueur']=demande_joueur_ordinateur(i+1)
        donnee_joueur['score']=0
        donnee_joueur['point_plancher_manche_pre']=0
        donnee_joueur['point_mosaique_manche_pre']=0
        
        lst_donnee_joueur.append(donnee_joueur)
    return lst_donnee_joueur
