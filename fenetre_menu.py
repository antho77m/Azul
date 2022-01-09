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
    j="Charger une partie"
    texte(xa,ya,j,taille=20)
    rectangle(xa-15,ya-15,xb-50,yb-5,couleur="pink")
    

def select_type_j1(lst):
    while True :
        mise_a_jour()
        x, y, z = attente_clic()
        if x<=120+200 and x>=150-2 and y<=250+200-5 and y>=180+4: 
            lst.append("j")
            return True
        if x<=120+200 and x>=150-2+60 and y<=250+200-5 and y>=180+4+60:          
            lst.append("o")
            return True
        else:
            return False


def select_type_j2(lst):
    x, y, z = attente_clic()
    while True :
        if x>=120+200+200 and x<=150-2 and y>=250+200+200-5 and y<=180+4: 
            lst.append("j")
            return True
        if x>=120+200+200 and x<=150-2+60 and y>=250+200-5+200 and y<=180+4+60:          
            lst.append("o")
            return True
        else:
            return False

def select_type_j3(lst):
    x, y, z = attente_clic()
    while True :
        if x>=120+200+200+200 and x<=150-2 and y>=250+200+200+200-5 and y<=180+4: 
            lst.append("j")
            return True
        if x>=120+200+200+200 and x<=150-2+60 and y>=250+200-5+200+200 and y<=180+4+60:          
            lst.append("o")
            return True
        else:
            return False


def select_type_j4(lst):
    x, y, z = attente_clic()
    while True :
        if x>=120+200+200+200+200 and x<=150-2 and y>=250+200+200+200+200-5 and y<=180+4: 
            lst.append("j")
            return True
        if x>=120+200+200+200+200 and x<=150-2+60 and y>=250+200-5+200+200+200 and y<=180+4+60:          
            lst.append("o")
            return True
        else:
            return False

if __name__ == '__main__':

    cree_fenetre(1000,600)
    lst_j=[]
    lst_jouer=[]
    titrejeux()
    jouer(790,500)
    savepart(50,510)
    mise_a_jour()
    while True:
        if len(lst_jouer)==0:
            colonne_joueur(0,125,150,"blue")
            mise_a_jour()
            select_type_j1(lst_jouer)
            
        if len(lst_jouer)==1:
            colonne_joueur(0,125,150,"green")
            colonne_joueur(1,125*2,150,"blue")
            select_type_j2(lst_jouer)
        if len(lst_jouer)==2:
            colonne_joueur(1,125*2,150,"green")
            colonne_joueur(2,125*3,150,"blue")
            select_type_j3(lst_jouer)
        if len(lst_jouer)==3:
            colonne_joueur(2,125*3,150,"green")
            colonne_joueur(3,125*4,150,"blue")
            select_type_j4(lst_jouer)
        if len(lst_jouer)==4:
            colonne_joueur(3,125*4,150,"green")
        

    print(lst_jouer)
    attente_clic()
    ferme_fenetre()






