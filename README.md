# tictactoe-python
# Intelligent Tic-Tac-Toe Game (Unbeatable AI)

A desktop-based Tic-Tac-Toe application built in Python using the `Tkinter` framework. The project features a modular architecture, persistent state tracking across games, and an optimized, rule-based deterministic AI subsystem designed to be completely unbeatable.

## Features

- **Modular Design:** Complete separation of concerns between the onboarding menu and configuration dashboard (`main.py`) and the core execution engine (`joc_greu.py`).
- **Unbeatable AI Engine:** Programmed with a multi-layered rule matrix that actively calculates win vectors, immediate threat blocks, corner/edge heuristics, and center-board control.
- **Persistent State Management:** Tracks real-time player statistics (Win/Loss scores) and a dynamic virtual wallet system ($10 EUR reward per victory) across continuous game iterations.
- **Clean State Transitions:** Utilizes event-driven window orchestration techniques (`.withdraw()` and `.wait_window()`) to manage the application lifecycle smoothly without resource or memory overhead.

## Project Structure

```text
├── main.py       # Application entry point, onboarding interface, and player turn configuration
└── joc_greu.py   # Core gameplay logic, UI rendering loop, and AI decision-making matrix
