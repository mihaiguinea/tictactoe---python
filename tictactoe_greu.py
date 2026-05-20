import tkinter as tk
import joc_greu as joc

def porneste_joc(cine_incepe):
    # Hide the menu window instead of destroying it
    meniu.withdraw() 
    
    # Start the game directly with the Unbeatable (Hard) variant
    joc.start_joc(cine_incepe) 
    
    # Wait until the window from joc.py is closed
    meniu.wait_window(joc.fereastra_joc)
    
    # Redisplay the main menu window after the match ends
    meniu.deiconify()

# --- WINDOW CREATION ---
meniu = tk.Tk()
meniu.title("Setări Joc - Mod Imbatabil")
meniu.geometry("806x650")

# Maintained your original layout but brought the options directly onto the screen
frame_inceput = tk.Frame(meniu)
frame_inceput.pack(pady=80)

tk.Label(frame_inceput, text="X și 0 - Mod Greu", font=('Arial', 40, 'bold')).pack(pady=20)
tk.Label(frame_inceput, text="Cine mută primul?", font=('Arial', 30, 'bold')).pack(pady=30)

btn_incepe_x = tk.Button(frame_inceput, text="Eu (X) încep", width=25, font=('Arial', 25), command=lambda: porneste_joc("X"))
btn_incepe_x.pack(pady=10)

btn_incepe_o = tk.Button(frame_inceput, text="Botul (O) începe", width=25, font=('Arial', 25), command=lambda: porneste_joc("O"))
btn_incepe_o.pack(pady=10)

meniu.mainloop()
