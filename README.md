# Tic-Tac-Toe with Minimax AI (Pygame + NumPy)

## Overview
This project implements a **Tic-Tac-Toe game** with a graphical interface built using **Pygame**, where the computer opponent plays **perfectly** using the **Minimax algorithm**.  
The AI anticipates every possible move, ensuring that it **never loses** — it either wins or forces a draw.  

The project demonstrates the integration of **algorithmic game theory** with **interactive graphics**, blending logic and user experience into a clean Python implementation.

---

## Why Minimax?
Games like Tic-Tac-Toe are **zero-sum**, meaning one player’s gain is another’s loss.  
The **Minimax algorithm** provides the optimal strategy by exhaustively exploring all possible game outcomes.

### Key Advantages
- **Perfect Play** – AI always chooses the best possible move.
- **Deterministic** – No randomness; outcomes are fully explainable.  
- **Foundational Algorithm** – Basis for AI in chess, checkers, and Go.  

---

## Technologies Used
|------------|----------|
| **Python 3** | Core logic & scripting |
| **NumPy** | Efficient board state manipulation |
| **Pygame** | Graphical interface and event handling |
| **Algorithmic AI (Minimax)** | Decision-making for the computer opponent |

---

## System Design
### GameModel (Logic Layer)
- Manages board state as a NumPy array  
- Checks for valid moves, wins, and draws  
- Implements the **Minimax recursive search**  
- Provides `ai_move()` for optimal AI turns  

### Pygame Layer (View + Controller)
- Draws grid lines, O/X figures, and winning highlights  
- Handles user clicks and restart functionality  
- Displays messages like *“Player Wins!”*, *“AI Wins!”*, or *“Draw!”*

---

## How the Minimax Algorithm Works
Minimax is a **recursive decision algorithm** for two-player games.  
It assumes both players play optimally — one maximizes the score, the other minimizes it.

### Step-by-Step Process
1. **Simulate all possible moves** from the current board.  
2. **Recursively explore** resulting board states until reaching a terminal state:
   - AI win → `+1`  
   - Human win → `−1`  
   - Draw → `0`  
3. On AI’s turn → choose the **maximum** score.  
   On Human’s turn → choose the **minimum** score.  
4. Return the best score up the recursion tree to select the final move.
