from Azul_sys_memoire import fichier_existe
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
    

def select_type_j1(lst,x,y):
    if x>=120 and x<=245 and y>=210 and y<=240: 
        lst.append("j")
        return 
    if x>=120 and x<=245 and y>=270 and y<=300:          
        lst.append("o")
        return 


def select_type_j2(lst,x,y):
    if x>=310 and x<=430 and y>=210 and y<=240: 
        lst.append("j")
        return 
    if x>=310 and x<=430 and y>=270 and y<=300:          
        lst.append("o")
        return 

def select_type_j3(lst,x,y):
    if x>=490 and x<=615 and y>=210 and y<=240: 
        lst.append("j")
        return 
    if x>=490 and x<=615 and y>=270 and y<=300:          
        lst.append("o")
        return 


def select_type_j4(lst,x,y):
    if x>=680 and x<=800 and y>=210 and y<=240: 
        lst.append("j")
        return 
    if x>=680 and x<=800 and y>=270 and y<=300:          
        lst.append("o")
        return 

def select_charge(x,y):
    return 790+15-2>=x and x<=790-5 and 500+60+4>=y and y>=500

def select_jouer(x,y):
    return  x>=792 and x<=943 and y <=650 and y >=502

#792 502
#943 560


def menu_selection():
    
    cree_fenetre(1000,600)
    lst_j=[]
    lst_jouer=[]
    titrejeux()
    jouer(790,500)
    if fichier_existe():
        savepart(50,510)
    rectangle(790,500,790+150,500+60)
    x=0
    y=0
    colonne_joueur(0,125,150,"blue")
    
    
    while True:

        x, y, z = attente_clic()
        
        if select_charge(x,y) and fichier_existe():
            ferme_fenetre()
            return 
        if select_jouer(x,y) and len(lst_jouer)!=0:
            ferme_fenetre()
            return lst_jouer

        if len(lst_jouer)==0:
            colonne_joueur(0,125,150,"blue")
            select_type_j1(lst_jouer,x,y)
            continue
        if len(lst_jouer)==1:
            colonne_joueur(0,125,150,"green")
            colonne_joueur(1,125*2+60,150,"blue")
            select_type_j2(lst_jouer,x,y)
            continue
        if len(lst_jouer)==2:
            colonne_joueur(1,125*2+60,150,"green",)
            colonne_joueur(2,125*3+60*2,150,"blue",)
            select_type_j3(lst_jouer,x,y)
            continue 
        if len(lst_jouer)==3:
            colonne_joueur(2,125*3+60*2,150,"green")
            colonne_joueur(3,125*4+60*3,150,"blue")
            select_type_j4(lst_jouer,x,y)
            continue
        if len(lst_jouer)==4:
            colonne_joueur(3,125*4+60*3,150,"green")
        
        
if __name__ == '__main__':
        print(menu_selection())
        
