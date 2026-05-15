"""
@author: Kouachi Corneille EKON
@date: 12/05/2026

------------------------------------------------------

Conway's Game of Life avec interface graphique (Tkinter)
--------------------------------------------------------

Fonctionnalités :
- Interface graphique
- Démarrage / Pause
- Génération aléatoire
- Réinitialisation
- Affichage en temps réel

"""


from functions import *

# =========================
# CONFIGURATION
# =========================
CELL_SIZE = 25
ROWS = 60
COLS = 60

DELAY = 100  # ms entre chaque génération

ALIVE_COLOR = "black"
DEAD_COLOR = "white"



# =========================
# PROGRAMME PRINCIPAL
# =========================
if __name__ == "__main__":

    root = tk.Tk()

    game = GameOfLife(root)

    root.mainloop()

