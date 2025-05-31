# MindGrid: AI Tic Tac Showdown

**MindGrid** is a Python-based intelligent Tic Tac Toe game with a twist — you face off against an unbeatable AI powered by the **Minimax algorithm**. Designed with a clean **PyGame** interface and strategic logic, the game offers an engaging experience of classic Tic Tac Toe where every move counts.

## Features

-  **AI Opponent** using the Minimax algorithm (cannot be beaten!)
-  **Graphical Interface** built with PyGame
-  **Win Detection** (rows, columns, diagonals)
-  **Restart Option** via button click
-  **Winning Animation** with victory text zoom-in
-  **Fully Functional Game Logic** written from scratch with NumPy

## How the AI Works (Minimax)

The AI uses a **recursive Minimax algorithm** that:
- Simulates all possible game states
- Assigns scores: +1 (AI win), -1 (Player win), 0 (Draw)
- Chooses the best move that maximizes its winning chances

This ensures:
- AI always wins or draws if played optimally
- AI never loses

![image](https://github.com/user-attachments/assets/cb54a2f5-4697-4ac3-9f35-e30000c0662b)

![image](https://github.com/user-attachments/assets/3bd05f7c-d855-4c4f-97a7-2fef389f4e62)
