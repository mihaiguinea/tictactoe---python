import tkinter as tk
from tkinter import messagebox
import random

# Global variables
tabla = []
butoane = []
jucator_curent = ""
fereastra_joc = None

# New variables for the scoring system and financial balance
scor_om = 0
scor_bot = 0
balanta = 0

def verifica_victorie(simbol):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == simbol: return True
    for j in range(3):
        if tabla[0][j] == tabla[1][j] == tabla[2][j] == simbol: return True
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == simbol: return True
    if tabla[0][2] == tabla[1][1] == tabla[2][0] == simbol: return True
    return False

def verifica_remiza():
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == " ": return False
    return True

def dezactiveaza_butoane():
    for i in range(3):
        for j in range(3):
            butoane[i][j].config(state=tk.DISABLED)

def gaseste_mutare_critica(simbol):
    for i in range(3):
        rand=[tabla[i][0], tabla[i][1],tabla[i][2]]
        if rand.count(simbol)== 2 and rand.count(" ")==1:
            spatiu_gol=rand.index(" ")
            return (i, spatiu_gol)
    for i in range(3):
        col=[tabla[0][i], tabla [1][i], tabla[2][i]]
        if col.count(simbol)==2 and col.count(" ")==1:
            spatiu_gol_col=col.index(" ")
            return(spatiu_gol_col, i)
    diag1=[tabla[0][0], tabla[1][1], tabla[2][2]]
    if diag1.count(simbol)==2 and diag1.count(" ")==1:
        spatiu_diag1=diag1.index(" ")
        return( spatiu_diag1, spatiu_diag1)
    diag2=[tabla[0][2], tabla[1][1], tabla[2][0]]
    if diag2.count(simbol)==2 and diag2.count(" ")==1:
        spatiu_diag2=diag2.index(" ")
        return (spatiu_diag2, 2-spatiu_diag2)
    return None

def verify_diag():
    if tabla[0][0]!=" " and tabla[1][1]!=" " and tabla[2][2]!=" ":
        lista_colt=[(0,0), (2,2), (0,2), (2,0)]
        colt_liber=[c for c in lista_colt if tabla[c[0]][c[1]]==" "]
        if colt_liber:
             return random.choice(colt_liber)
    elif  tabla[0][2]!=" " and tabla[1][1]!=" " and tabla[2][0]!=" ":
        lista_colt=[(0,0), (2,2), (0,2), (2,0)]
        colt_liber=[c for c in lista_colt if tabla[c[0]][c[1]]==" "]
        if colt_liber:
             return random.choice(colt_liber)
    else:
        return None

def verify_diag2():
    if tabla[0][0]!=" " and tabla[1][1]!=" " and tabla[2][2]!=" ":
        marg=[(0,1), (1,0), (1,2), (2,1)]
        marg_liber=[c for c in marg if tabla[c[0]][c[1]]==" "]
        if marg_liber:
             return random.choice(marg_liber)
    elif  tabla[0][2]!=" " and tabla[1][1]!=" " and tabla[2][0]!=" ":
        marg=[(0,1), (1,0), (1,2), (2,1)]
        marg_liber=[c for c in marg if tabla[c[0]][c[1]]==" "]
        if marg_liber:
             return random.choice(marg_liber)
    else:
        return None

def colt(i,j):
    lista_colt=[(0,2), (2,0), (2,2), (0,0)]
    pereche_scos=(i,j)
    if pereche_scos in lista_colt:
        lista_colt.remove(pereche_scos)
    return random.choice(lista_colt)

def verif_marg():
    marg=[tabla[1][0],tabla[1][2]]
    marg_idx=[(1,0), (1,2)]
    marg2=[tabla[0][1],  tabla [2][1]]
    marg2_idx=[(0,1),(2,1)]
    if marg.count(" ") > marg2.count(" "):  
        return random.choice(marg_idx)
    elif  marg.count(" ") < marg2.count(" "):
        return random.choice(marg2_idx)
    else:
        for i in range(3):
            for j in range (3):
                row_liber=[tabla[i][0], tabla[i][1], tabla[i][2]]
                col_liber=[tabla[0][j], tabla[1][j], tabla[2][j]]
                if row_liber.count(" ")== 3 and col_liber.count(" ")==3 :
                 return colt(i,j)

def mutare_bot():
    global jucator_curent, scor_bot
    
    pozitii_libere = [(i, j) for i in range(3) for j in range(3) if tabla[i][j] == " "]
    if not pozitii_libere: return

    # Bot AI Logic (Hard Difficulty)
    aux=gaseste_mutare_critica('O')
    diag_mutare = verify_diag()
    
    if aux:
        rand, coloana=aux
    elif gaseste_mutare_critica('X'):
        rand,coloana=gaseste_mutare_critica('X')
    elif len(pozitii_libere) == 8 and tabla[1][1] == "X":
