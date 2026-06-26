# Snake

A feature-rich implementation of the classic Snake game written in Python using Pygame. 
The project includes both a graphical version and a console version while sharing the same game logic.

## Features

- Modern Pygame graphical interface
- Console version
- Multiple game modes
  - **Regular** – Play predefined levels followed by endless randomly generated levels.
  - **Classic** – Complete all handcrafted levels.
  - **Random** – Endless randomly generated obstacle layouts.
- Three speed settings
- Multiple visual themes
  - Default
  - Retro
  - Cyberpunk
- Level progression through gates
- Dynamic obstacle generation
- Random food spawning
- Level and snake length tracking

---

### Requirements

- Python 3.10+
- pygame
- numpy
- readchar

Install dependencies:

```bash
pip install pygame numpy readchar
```

---

## Running the Game

In the snake directory run:

```bash
python main.py
```

---

## Running the Tests

### Requirements:

-Pytest

In the outer directory run:

```bash
pytest -o pythonpath=snake
```

---

## Controls

### Gameplay

Tap the arrow keys for mmovement

---

## Game Modes

### Regular

Starts with handcrafted levels and automatically continues into infinitely generated random levels.

### Classic

Play through all handcrafted levels. The game ends after the final level has been completed.

### Random

Generates random obstacle layouts indefinitely for endless gameplay.

---

## Themes

### Default

Black and green combination.

### Retro

Game Boy inspired monochrome palette.

### Cyberpunk

Bright neon colors with a futuristic style.

---

## Gameplay

- Control the snake using the arrow keys.
- Eat food to grow longer.
- Avoid walls, obstacles and your own body.
- After reaching a sufficient length, a gate appears.
- Entering the gate advances to the next level.
- Each level introduces new obstacle layouts.
- If the snake goes too long without eating, it gradually shrinks.

---

## Technologies

- Python
- Pygame
- NumPy
- readchar

---

## Project Architecture

The project separates game mechanics from rendering:

- **game_logic.py**
  - snake movement
  - collision detection
  - food spawning
  - level progression
  - gate mechanics

- **gui.py**
  - rendering
  - menus
  - themes
  - user input

- **console_loop.py**
  - terminal rendering
  - keyboard input
  - shared gameplay logic
    
- **levels.py**
  - defines obstacles
  - generate classical and random levels

- **main.py**
  - chooses a proper evrionment
  - starts the game

This separation allows the same gameplay implementation to be used in multiple interfaces.

---

## Author

Created by **Alharf42**.
