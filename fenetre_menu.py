from upemtk import *

def colonne_joueur(num,xa,ya,couleurj):
    selecJ(num,xa,ya,couleurj)
    selecNIA(xa,ya+60)
    selecIA(xa,ya+120)


def jouer(xa,ya):
    yb=ya+60
    xb=xa+150
    j="Jouer"
    texte(xa,ya,j,taille=40)
    rectangle(xa-5,ya-2,xb,yb+4,couleur="pink")


def selecJ(num,xa,ya,couleurj):
    yb=ya+30
    xb=xa+120
    j="joueur : " + str(num+1)
    texte(xa,ya,j,taille=20)
    rectangle(xa-5,ya-2,xb,yb+4,couleur=couleurj)


def selecIA(xa,ya):
    yb=ya+30
    xb=xa+120
    j="IA"
    texte(xa,ya,j,taille=20)
    rectangle(xa-5,ya-2,xb,yb+4)


def selecNIA(xa,ya):
    yb=ya+30
    xb=xa+120
    j="Joueur"
    texte(xa,ya,j,taille=20)
    rectangle(xa-5,ya-2,xb,yb+4)

def titrejeux():
    xa=410
    ya=20
    j="AZUL"
    texte(xa,ya,j,taille=50)

def savepart(xa,ya):
    yb=ya+60
    xb=xa+300
    j="Sauvgarder une partite"
    texte(xa,ya,j,taille=20)
    rectangle(xa-15,ya-15,xb,yb-5,couleur="pink")
    

def select_type_j1():
    while True :
        joueur_ia1=attente_clic() #sensé etre les coordoné de la case IA du joureur choisie
        joueur_simple1=attente_clic() #sensé etre les coordoné de la case joueur sans IA du joureur choisie
        if joueur_ia1==joueur_ia1: 
            return joueur_ia1
        if joueur_simple1==joueur_simple1:
            return joueur_simple1

def select_type_j2():
    while True :
        joueur_ia2=attente_clic()#idem
        joueur_simple2=attente_clic()#idem
        if joueur_ia2==joueur_ia2:
            return joueur_ia2
        if joueur_simple2==joueur_simple2:
            return joueur_simple2

def select_type_j3():
    while True :
        joueur_ia3=attente_clic()
        joueur_simple3=attente_clic()
        if joueur_ia3==joueur_ia3:
            return joueur_ia3
        if joueur_simple3==joueur_simple3:
            return joueur_simple3


def select_type_j4():
    while True :
        joueur_ia4=attente_clic()
        joueur_simple4=attente_clic()
        if joueur_ia4==joueur_ia4:
            return joueur_ia4
        if joueur_simple4==joueur_simple4:
            return joueur_simple4

if __name__ == '__main__':

    cree_fenetre(1000,600)
    titrejeux()
    w=125
    jouer(790,500)
    savepart(50,510)
    for i in range(4):
        colonne_joueur(i,w,150,"blue")
        if i==0:
            select_type_j1()
            colonne_joueur(i,w,150,"green")
        if i==1:
            select_type_j2()
            colonne_joueur(i,w,150,"green")
        if i==2:
            select_type_j3()
            colonne_joueur(i,w,150,"green")
        if i==3:
            select_type_j4()
            colonne_joueur(i,w,150,"green")
        w=w+200

    attente_clic()
    ferme_fenetre()