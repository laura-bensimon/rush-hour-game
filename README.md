# Rush Hour – Python OOP Puzzle Game

A full Object-Oriented implementation of the classic **Rush Hour** puzzle, developed as part of the Hebrew University CS course *Introduction to Computer Science*.

The game models cars on a 7×7 board, enforces movement rules, validates movements, prevents collisions, and simulates the logic of the puzzle.

---

##  Features

###  Object-Oriented Architecture  
- `Car` class: orientation, length, allowed moves.  
- `Board` class: placement, movement validation, illegal-move detection, collision checks.  
- `Game` class: game controller, user input parsing, winning condition.  
- `helper.py`: shared utility functions.

###  JSON Configuration  
The initial state of the board is defined in `car_config.json`.

###  Input Validation  
- Prevents illegal movements  
- Ensures cars do not overlap  
- Ensures cars remain inside the game boundaries

###  Complete Testing Suite  
Included unit tests covering:
- Car mechanics  
- Board logic  
- Game flow  
- Combined scenarios  

---

##  Skills Demonstrated  
- Object-Oriented Programming (classes, encapsulation, modularity)  
- Clean software architecture  
- Game logic & rule enforcement  
- JSON parsing  
- Defensive programming  
- Software testing (pytest)

---
##  Repository Structure
src/
  car.py
  board.py
  game.py
  helper.py
  car_config.json

tests/
  _test_car.py
  _test_board.py
  _test_game.py
  _test_wboard_game.py
  _test_wcar_board.py
  _test_wcar_game.py
  _test_wcar_wboard_game.py
  
------

##  Author
Laura Bensimon  
Computer Science and Data Science student  
Hebrew University of Jerusalem

