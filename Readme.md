# Conway's Game of Life

**Author:** Kouachi Corneille EKON
**Date:** 12/05/2026

---

## Description

Conway's Game of Life built with Python and Tkinter.
The grid evolves generation by generation according to the classic rules:

- A live cell with 2 or 3 neighbors survives.
- A dead cell with exactly 3 neighbors becomes alive.
- All other cells die or stay dead.

---

## Project Structure

```
MIT_Broadening_RV/
├── main.py         # Entry point — window setup and game loop
├── functions.py    # GameOfLife class (grid logic + rendering)
├── game.sh         # Launch script (checks dependencies, runs main.py)
└── Readme          # This file
```

### Role of each file

| File | Role |
|---|---|
| `main.py` | Creates the Tk window, instantiates `GameOfLife`, starts the event loop |
| `functions.py` | Contains the `GameOfLife` class: grid, drawing, rules, controls |
| `game.sh` | Shell script that verifies Python3 and tkinter, then launches `main.py` |

---

## How to Launch

### With the shell script (recommended)

```bash
chmod +x game.sh   # only needed once
./game.sh
```

The script automatically checks and installs missing dependencies (`python3`, `python3-tk`) before launching the program.

### Directly with Python

```bash
python3 main.py
```

> Requires Python 3 and tkinter (`sudo apt install python3-tk` on Debian/Ubuntu if missing).

---

## Controls

| Button | Action |
|---|---|
| **Start** | Start the simulation |
| **Pause** | Pause the simulation |
| **Random** | Fill the grid randomly |
| **Clear** | Reset the grid (all cells dead) |
| Mouse click | Toggle a cell alive / dead |

---

## Dependencies

| Library | Source | Notes |
|---|---|---|
| `tkinter` | Python standard library | May need `python3-tk` on Linux |
| `random` | Python standard library | Built-in, no install needed |
