import tkinter as tk
import joc_greu as joc

def porneste_joc(cine_incepe):
    # Ascundem fereastra meniului în loc să o distrugem
    meniu.withdraw() 
    
    # Pornim jocul cu varianta Imbatabil (Greu) direct
    joc.start_joc(cine_incepe) 
    
    # Așteptăm până când fereastra din joc.py este închisă
    meniu.wait_window(joc.fereastra_joc)
    
    # Reafișăm fereastra meniului principal după terminarea meciului
    meniu.deiconify()

# --- CREAREA FERESTREI ---
meniu = tk.Tk()
meniu.title("Setări Joc - Mod Imbatabil")
meniu.geometry("806x650")

# Am păstrat structura ta, dar am adus opțiunile direct pe ecran
frame_inceput = tk.Frame(meniu)
frame_inceput.pack(pady=80)

tk.Label(frame_inceput, text="X și 0 - Mod Greu", font=('Arial', 40, 'bold')).pack(pady=20)
tk.Label(frame_inceput, text="Cine mută primul?", font=('Arial', 30, 'bold')).pack(pady=30)

btn_incepe_x = tk.Button(frame_inceput, text="Eu (X) încep", width=25, font=('Arial', 25), command=lambda: porneste_joc("X"))
btn_incepe_x.pack(pady=10)

btn_incepe_o = tk.Button(frame_inceput, text="Botul (O) începe", width=25, font=('Arial', 25), command=lambda: porneste_joc("O"))
btn_incepe_o.pack(pady=10)

meniu.mainloop()