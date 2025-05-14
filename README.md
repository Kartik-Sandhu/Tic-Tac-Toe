### **Tic-Tac-Toe Game (2 Players) - Terminal-Based**

This Python project implements the classic **Tic-Tac-Toe** game for two players in a terminal or command-line interface. Players take turns choosing positions on a 3x3 grid, where one player uses the symbol `X` and the other uses `O`.

#### **Game Flow:**

1. **Board Setup:**

   * The board is represented as a list of 9 elements, all initialized to empty spaces `' '`.
   * Each cell in the list corresponds to a position on the grid (1-9).

2. **Turn-Based Gameplay:**

   * Player 1 (X) and Player 2 (O) alternate turns.
   * Each player selects a position (1–9), which corresponds to a spot on the 3x3 grid.
   * The game ensures only valid moves are accepted (empty positions).

3. **Winning Conditions:**

   * The game checks for a winner after every move. A player wins if they manage to place their symbol in a row, column, or diagonal containing three of their symbols.

4. **Draw Condition:**

   * If all positions are filled without a winner, the game ends in a draw.

5. **Game Restart:**

   * After a game ends, players are prompted whether they want to play again.

#### **Features:**

* **Board Display:** The board is printed after every move, showing the current state of the game.
* **Input Validation:** The game checks for invalid moves, like choosing already taken positions or entering numbers outside the range (1-9).
* **Replay Option:** After a win or draw, players can decide whether they want to play another round.

#### **Tools and Concepts Used:**

* **Functions:** To handle logic like printing the board, checking win conditions, and managing the flow of the game.
* **Lists:** Used to store and update the state of the board.
* **Loops and Conditionals:** For repeating turns, checking for a winner, and managing the game flow.
* **User Input:** Players provide input through the console to make their moves.

#### **How to Play:**

1. Run the Python script in your terminal or Jupyter notebook.
2. Players take turns selecting positions (1-9) to place their symbols.
3. The game ends when one player wins or the game ends in a draw.
4. Players can start a new game after each round.



