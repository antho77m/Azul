from Azul_sys_avant_jeu import initialisation_plancher

def ligne_complete(ligne):
    for tuile in ligne:
        if not tuile_remplie(tuile):
            return False
    return True

def verif_ligne_mosaique_complete(mosaique):
    for ligne in mosaique:
        if ligne_complete(ligne):
            return True
    return False

def condition_fin(sac_tuile,donnee_joueur):
    if not sac_tuile:
        return True
    for joueur in donnee_joueur:
        if verif_ligne_mosaique_complete(joueur['mosaique']):
            return True

    return False

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




def qui_commence(liste_donnee_joueur):
    ''' 
    renvoie un nombre pour faire jouer le joueur qui doit commencer la nouvelle manche
    '''
    for i in range(len(liste_donnee_joueur)):
        if -1 in liste_donnee_joueur[i]['plancher']: 
            return i
    return 0
        


        ######################
        # fonction utilisez  #
        # apres une manche   #
        ######################
def ligne_motif_remplis(ligne):
    return not(0 in ligne)

def vide_ligne_motif(ligne):
    for i in range(len(ligne)):
        ligne[i]=0

def vide_motif_joueur(motif):
    liste_ligne_videe_et_val=[]
    for i in range(5):
        if ligne_motif_remplis(motif[i]):
            liste_ligne_videe_et_val.append((i,motif[i][0])) 
            #stockage de la ligne supprimé ainsi que la valeur de la tuile
            vide_ligne_motif(motif[i])
    return liste_ligne_videe_et_val
    
def complete_mosaique(ligne_mosaique_maj,mosaique):
    for e in ligne_mosaique_maj:    #pour chaque tuple dans la liste
        val_tuile_correspondante=e[1]+5
        for i in range(5):
            num_ligne=e[0]
            if mosaique[num_ligne][i]==val_tuile_correspondante:
                mosaique[num_ligne][i]=e[1]
                break

def action_motif_joueur(motif,mosaique):
    ligne_mosaique_maj=vide_motif_joueur(motif)
    complete_mosaique(ligne_mosaique_maj,mosaique)

def compte_point_plancher(plancher,point_plancher):
    #renvoit les point stocker dans le placher
    equivalent_point_plancher=[-1,-1,-2,-2,-2,-3,-3]
    
    for i in range(len(plancher)):
        if plancher[i]!=0 :
            point_plancher+=equivalent_point_plancher[i]
        else:
            break
    return point_plancher

def tuile_remplie(tuile):
    return tuile>0 and tuile<6

def case_dans_matrice(M,i,j):
    '''fonction regardant si les indice donné sont dans la matrice'''
    if i>=len(M) or i<0:
        return False
    if j>=len(M) or j<0:
        return False
    return True

def calcul_score_tuile_droit(mosaique_manche_pre,i,j):
    score=0
    if case_dans_matrice(mosaique_manche_pre, i, j) and tuile_remplie(mosaique_manche_pre[i][j]):
        return calcul_score_tuile_droit(mosaique_manche_pre, i+1, j)+1
    return score

def calcul_score_tuile_gauche(mosaique_manche_pre,i,j):
    score=0
    if case_dans_matrice(mosaique_manche_pre, i, j) and tuile_remplie(mosaique_manche_pre[i][j]):
        return calcul_score_tuile_droit(mosaique_manche_pre, i-1, j)+1
    return score

def calcul_score_tuile_bas(mosaique_manche_pre,i,j):
    score=0
    if case_dans_matrice(mosaique_manche_pre, i, j) and tuile_remplie(mosaique_manche_pre[i][j]):
        return calcul_score_tuile_droit(mosaique_manche_pre, i, j+1)+1
    return score

def calcul_score_tuile_haut(mosaique_manche_pre,i,j):
    score=0
    if case_dans_matrice(mosaique_manche_pre, i, j) and tuile_remplie(mosaique_manche_pre[i][j]):
        return calcul_score_tuile_droit(mosaique_manche_pre, i, j-1)+1
    return score

def score_tuile(mosaique_manche_pre,i,j):
    score=1
    score+=calcul_score_tuile_droit(mosaique_manche_pre, i+1, j)
    score+=calcul_score_tuile_gauche(mosaique_manche_pre, i-1, j)
    score+=calcul_score_tuile_bas(mosaique_manche_pre, i, j+1)
    score+=calcul_score_tuile_haut(mosaique_manche_pre, i, j-1)
    return score

def compte_point_mosaique(mosaique,mosaique_manche_pre):
    score=0
    for i in range(len(mosaique)):
        for j in range(len(mosaique)):
            if mosaique[i][j]!=mosaique_manche_pre[i][j]:
                score+=score_tuile(mosaique_manche_pre,i,j)
                mosaique_manche_pre[i][j]=mosaique[i][j]
    return score

def compte_point_tout_joueur(liste_donnee_joueur):
    for joueur in liste_donnee_joueur:
        joueur['score']=compte_point_joueur(joueur['point_mosaique_manche_pre'], joueur['plancher'], joueur['point_plancher_manche_pre'])

def compte_point_joueur(point_mosaique,plancher,point_plancher_manche_precedente):
    #renvoit les point d'un joueur
    point_plancher=compte_point_plancher(plancher,point_plancher_manche_precedente)
    score=point_plancher+point_mosaique

    return score


def action_fin_manche(donnee_joueur):
    '''
    fonction réalisant les différentes actions a faire sur les joueur a la fin d'une manche.
    '''


    for joueur in donnee_joueur:
        #enleve les ligne motif pleine
        action_motif_joueur(joueur['motif'], joueur['mosaique'])
        
        joueur['score']=compte_point_joueur(joueur['point_mosaique_manche_pre'],joueur['plancher'],joueur['point_plancher_manche_pre'])
        joueur['point_plancher_manche_pre']=compte_point_plancher(joueur['plancher'],joueur['point_plancher_manche_pre'])
        joueur['point_mosaique_manche_pre']+=compte_point_mosaique(joueur['mosaique'],joueur['mosaique_manche_pre'])
        joueur['plancher']=initialisation_plancher()

