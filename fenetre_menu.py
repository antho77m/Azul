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
    

# univ upem

if __name__ == '__main__':

    cree_fenetre(1000,600)
    titrejeux()
    w=125
    for i in range(4):
        colonne_joueur(i,w,150,"blue")
        w=w+200
    jouer(790,500)
    savepart(50,510)

    attend_clic_gauche()
    ferme_fenetre()