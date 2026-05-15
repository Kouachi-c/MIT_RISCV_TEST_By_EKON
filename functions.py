"""
@author: Kouachi Corneille EKON
@date: 12/05/2026
------------------------------------------------------
Conway's Game of Life with graphical interface (Tkinter)
------------------------------------------------------
Fonctionnalities :
- graphical interface
- Start / Pause
- Random generation
- Reset
- Real-time display
"""
import tkinter as tk
import random

CELL_SIZE = 20
ROWS = 40
COLS = 40

DELAY = 100  # ms between generations

ALIVE_COLOR = "black"
DEAD_COLOR = "white"


class GameOfLife:

    def __init__(self, root):

        self.root = root
        self.root.title("Conway's Game of Life")

        self.running = False

        # grid
        self.grid = [
            [0 for _ in range(COLS)]
            for _ in range(ROWS)
        ]

        # graphic canvas
        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg="white"
        )
        self.canvas.pack()

        # Buttons
        controls = tk.Frame(root)
        controls.pack()

        tk.Button(
            controls,
            text="Start",
            command=self.start
        ).pack(side=tk.LEFT)

        tk.Button(
            controls,
            text="Pause",
            command=self.pause
        ).pack(side=tk.LEFT)

        tk.Button(
            controls,
            text="Random",
            command=self.randomize
        ).pack(side=tk.LEFT)

        tk.Button(
            controls,
            text="Clear",
            command=self.clear
        ).pack(side=tk.LEFT)

        # Initial drawing
        self.draw_grid()

        # Mouse click to activate/deactivate cell
        self.canvas.bind("<Button-1>", self.toggle_cell)

    # =====================================================
    # ITERATION SECTION
    # =====================================================
    # This function traverses the entire grid
    # with nested loops to draw

    # each cell on the screen.
    # =====================================================
    def draw_grid(self):
        """
        Draw the grid on the canvas.
        """

        self.canvas.delete("all")

        for row in range(ROWS):
            for col in range(COLS):

                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = (
                    ALIVE_COLOR
                    if self.grid[row][col]
                    else DEAD_COLOR
                )

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="gray"
                )

    def toggle_cell(self, event):
        """
        Toggle the state of a cell based on mouse click.
        """

        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if 0 <= row < ROWS and 0 <= col < COLS:
            self.grid[row][col] ^= 1
            self.draw_grid()

    def randomize(self):
        """
        Fill the grid with random alive/dead cells.
        """

        # =====================================================
        # ITERATION SECTION
        # =====================================================
        # double loop used to fill the grid with random 0 and 1.
        #
        # =====================================================
        for row in range(ROWS):
            for col in range(COLS):
                self.grid[row][col] = random.randint(0, 1)

        self.draw_grid()

    def clear(self):
        """
        Reset the grid to all dead cells.
        """

        # =====================================================
        # ITERATION SECTION
        # =====================================================
        # double loop used to reset all cells to 0 (dead).
        # =====================================================
        for row in range(ROWS):
            for col in range(COLS):
                self.grid[row][col] = 0

        self.draw_grid()

    def count_neighbors(self, row, col):

        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if i == 0 and j == 0:
                    continue

                r = row + i
                c = col + j

                if 0 <= r < ROWS and 0 <= c < COLS:
                    neighbors += self.grid[r][c]

        return neighbors

    def next_generation(self):

        """
        Compute the next generation based on the current grid state.
        """

        new_grid = [
            [0 for _ in range(COLS)]
            for _ in range(ROWS)
        ]

        # =====================================================
        # ITERATION SECTION
        # =====================================================
        # Parcours complet de la grille pour appliquer
        # les règles du Game of Life.
        # =====================================================
        for row in range(ROWS):
            for col in range(COLS):

                neighbors = self.count_neighbors(row, col)

                if self.grid[row][col] == 1:

                    # Survie
                    if neighbors in [2, 3]:
                        new_grid[row][col] = 1

                else:

                    # Reproduction
                    if neighbors == 3:
                        new_grid[row][col] = 1

        self.grid = new_grid

    # =====================================================
    # RECURSION SECTION
    # =====================================================
    # This function uses recursion to update the grid at regular intervals
    # when the simulation is running.
    # =====================================================
    def update(self):
        """
        Update the grid and redraw it if the simulation is running.
        """

        if self.running:

            self.next_generation()
            self.draw_grid()

            # Schedule the next update after a delay
            self.root.after(DELAY, self.update)

    def start(self):
        """
        Start the simulation.
        """

        if not self.running:
            self.running = True
            self.update()

    def pause(self):
        """
        Pause the simulation.
        """

        self.running = False


