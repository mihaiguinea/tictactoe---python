import tkinter as tk
from tkinter import messagebox
import random

# Variabile globale
tabla = []
butoane = []
jucator_curent = ""
fereastra_joc = None

# Variabile noi pentru sistemul de scor și balanță
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

    # Logica Botului (Dificultate Greu)
    aux=gaseste_mutare_critica('O')
    diag_mutare = verify_diag()
    
    if aux:
        rand, coloana=aux
    elif gaseste_mutare_critica('X'):
        rand,coloana=gaseste_mutare_critica('X')
    elif len(pozitii_libere) == 8 and tabla[1][1] == "X":
        lista_colt = [(0,0), (2,2), (0,2), (2,0)]
        rand, coloana = random.choice(lista_colt)
    elif tabla[1][0] =="X" and len(pozitii_libere)==8:
        rand,coloana=random.choice([(0,0), (2,0)])
    elif tabla[0][1] == "X" and len(pozitii_libere)==8:
        rand,coloana=random.choice([(0,0), (0,2)])
    elif tabla[1][2]== "X" and len(pozitii_libere)==8:
        rand,coloana=random.choice([(0,2),(2,2)])
    elif tabla[2][1] == "X" and len(pozitii_libere)==8:
        rand,coloana=random.choice([(2,0),(2,2)])
    elif tabla[1][0] =="X" and len(pozitii_libere)==7:
        rand,coloana=random.choice([(0,0), (2,0)])
    elif tabla[0][1] == "X" and len(pozitii_libere)==7:
        rand,coloana=random.choice([(0,0), (0,2)])
    elif tabla[1][2]== "X" and len(pozitii_libere)==7:
        rand,coloana=random.choice([(0,2),(2,2)])
    elif tabla[2][1] == "X" and len(pozitii_libere)==7:
        rand,coloana=random.choice([(2,0),(2,2)])
    elif tabla[1][1]==" ":
        rand,coloana=1,1
    elif len(pozitii_libere) == 6 and tabla[1][1] == "O" and tabla[0][0] == "X" and tabla[2][2] == " ":
        rand, coloana = 2, 2
    elif len(pozitii_libere) == 6 and tabla[1][1] == "O" and verify_diag2() :
        rand,coloana=verify_diag2()
    elif len(pozitii_libere)== 6 and ( tabla[1][0] =="X" or tabla[0][1] == "X" or tabla[1][2]== "X" or tabla[2][1] == "X"):
        rand,coloana=verif_marg()
    elif diag_mutare:
        rand,coloana=diag_mutare
    else:
        marg=[(1,0),(0,1),(1,2),(2,1)]
        marg_liber=[c for c in marg if tabla[c[0]][c[1]]==" "]
        
        if marg_liber:
            rand,coloana=random.choice(marg_liber)
        else:    
            lista_colt=[(0,0), (2,2), (0,2), (2,0)]
            colt_liber=[c for c in lista_colt if tabla[c[0]][c[1]]==" "]
            if colt_liber:
                rand,coloana=random.choice(colt_liber)
            else:
                rand,coloana=random.choice(pozitii_libere)
                
    # Executăm mutarea
    tabla[rand][coloana] = "O"
    butoane[rand][coloana].config(text="O", disabledforeground="black")
    
    if verifica_victorie("O"):
        dezactiveaza_butoane()
        scor_bot += 1
        messagebox.showinfo("Final", "Ai pierdut! Unlucky")
        fereastra_joc.destroy()
    elif verifica_remiza():
        messagebox.showinfo("Final", "Remiză!")
        fereastra_joc.destroy()
    else:
        jucator_curent = "X" # Rândul se întoarce la X

def click_buton(rand, coloana):
    global jucator_curent, scor_om, balanta
    
    # Permitem click-ul doar dacă spațiul e liber
    if tabla[rand][coloana] == " ":
        
        # Jucăm exclusiv cu botul, ignorăm click-ul omului dacă nu e rândul lui X
        if jucator_curent != "X":
            return
            
        # Efectuăm mutarea curentă a omului
        tabla[rand][coloana] = jucator_curent
        butoane[rand][coloana].config(text=jucator_curent)
        
        # Verificăm dacă omul a câștigat
        if verifica_victorie(jucator_curent):
            dezactiveaza_butoane()
            scor_om += 1
            balanta += 10
            messagebox.showinfo("Final", f"Felicitări, ai câștigat!\nAi primit 10 EUR.\nBalanță totală: {balanta} EUR")
            fereastra_joc.destroy()
            return
        elif verifica_remiza():
            messagebox.showinfo("Final", "Remiză!")
            fereastra_joc.destroy()
            return
            
        # Trecem la bot
        jucator_curent = "O"
        fereastra_joc.after(500, mutare_bot)

def start_joc(cine_incepe):
    global tabla, butoane, jucator_curent, fereastra_joc
    
    jucator_curent = cine_incepe # "X" sau "O"
    tabla = [[" " for _ in range(3)] for _ in range(3)]
    
    fereastra_joc = tk.Toplevel()
    fereastra_joc.title("Joc X și 0 - Mod Greu")
    
    # --- Secțiunea Scenariului și Balanței (afișată sus) ---
    frame_scor = tk.Frame(fereastra_joc)
    frame_scor.grid(row=0, column=0, columnspan=3, pady=10)
    
    tk.Label(frame_scor, text=f"Scor Om: {scor_om}  |  Scor Bot: {scor_bot}", font=('Arial', 14, 'bold')).pack()
    
    # Creăm butoanele
    butoane = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buton = tk.Button(
                fereastra_joc, text=" ", font=('Arial', 40, 'bold'), width=8, height=3,
                command=lambda r=i, c=j: click_buton(r, c)
            )
            # Folosim i+1 pentru rând ca să facem loc Frame-ului cu scor
            buton.grid(row=i+1, column=j)
            butoane[i][j] = buton

    # Dacă jucăm cu Botul și ai ales ca el să înceapă, îl punem să mute
    if jucator_curent == "O":
        fereastra_joc.after(500, mutare_bot)