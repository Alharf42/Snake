import readchar
import time
import msvcrt
from game_logic import (
    execute_game_logic, start_game, execute_game_logic, end_game, board, board_edges
)

# The console version of the game

# Board is a 2D grid
# Snake: list of tuples (coordinates(indeces) of the grid(board))
# Food just one tuple
# Create snake size 1x1 at the beginning
# Grows in length only by one and only when he eats food

# Snake's head is the first coordinate which can consume, crash,
# and starts movement and direction change
# Edges are on (1,y), (x,1), (20, y), (x, 20) coordinates
# Coordinates of food chosen randomely within the board size

# At start of the game set the size of the board

# When snake reaches a certain length he can get to next level trough gate
# which shows up after a certain length of the snake
# Game ends when snake will crash to himself or end of the board


# Reading keyboard
def get_optional_key():
    if msvcrt.kbhit():
        return readchar.readkey()
    else: 
        return None


def print_game(board, snake, food, obstacles, gate, level_tracker,
               board_edges):
    # Print the game in one static spot
    print("\033[H\033[J", end="")
    # When empty board .
    # when food *
    # when snake o
    print(f"=== CURRENT LEVEL: {level_tracker} ===")
    print()
    for i in range(0, len(board)-1):
        for j in range(0, len(board[1])-1):
            if (i, j) in snake:
                print(" o ", end="")
            elif (i, j) == food:
                print(" x ", end="")
            #elif (i, j) in board_edges:
            #    print(" ~ ", end="")
            elif (i, j) in obstacles:
                print(" ~ ", end="")
            elif (i, j) == gate:
                print(" D ", end="")
            else:
                print(" . ", end="")
        print()
    print()

# Choose mode-regular, classis, random
# Regular - Starts with the classic predetermined levels
# After those ends it continues with random levels to infinity
# Classic - contains only classic levels and ends after
# Random - only random infinite levels
# Level counter - display current level


def startUpMenu():

    # Displays an interactive startup menu allowing players to 
    # configure game speed and layout modes before launching

    speed_choices = {'1': ('Slow', 0.5), '2': ('Medium', 0.3),
                     '3': ('Fast', 0.1)}
    mode_choices = {'1': 'Regular', '2': 'Classic', '3': 'Random'}
    selected_speed_delay = 0.3
    selected_mode = 'Regular'

    # Menu loop for speed selection
    menu_active = True

    print("\033[H\033[J", end="")  # Clear console screen macro
    print("========================================")
    print("          S N A K E   G A M E           ")
    print("========================================")
    print(" CHOOSE YOUR SPEED:")
    for key, value in speed_choices.items():
        print(f"  [{key}] {value[0]}")
    print("----------------------------------------")
    print("Press 1, 2, or 3 to select...")
    while menu_active:    
        if msvcrt.kbhit():
            choice = msvcrt.getch().decode('utf-8', errors='ignore')
            if choice in speed_choices:
                selected_speed_delay = speed_choices[choice][1]
                menu_active = False

    # Menu loop for mode selection
    menu_active = True

    print("\033[H\033[J", end="")
    print("========================================")
    print("           SELECT GAME MODE             ")
    print("========================================")
    for key, value in mode_choices.items():
        print(f"  [{key}] {value}")
    print("----------------------------------------")
    print("Press 1, 2 or 3 to select...")
    while menu_active:    
        if msvcrt.kbhit():
            choice = msvcrt.getch().decode('utf-8', errors='ignore')
            if choice in mode_choices:
                selected_mode = mode_choices[choice]
                menu_active = False

    print("\033[H\033[J", end="")
    print("Configuration Saved! Game starting in 1 second...")
    time.sleep(1)

    return selected_speed_delay, selected_mode


def console_game():
    # If any other key than arrows is clicked it game overs
    speed, mode = startUpMenu()

    # Need to set physical time for each time step
    game_over = False
    direction = readchar.key.RIGHT
    not_eaten = 0
    obstacles = []
    level_tracker = 0
    gate = []
    inGate = False
    snake_head, snake, food = start_game(board, obstacles)
    print_game(board, snake, food, obstacles, gate, level_tracker, board_edges)
    while game_over is not True:

        # Ask for directions to user. Its optional, snake moves by default to right
        # User has only a limited time to insert direction, otherwise snake will move straight
        # That time is equal to the time of timestep
        key = get_optional_key()
        if key is not None:
            direction = key

        snake_head, snake, food, not_eaten, obstacles, level_tracker, gate, inGate = execute_game_logic(snake_head, snake, food, not_eaten, direction, obstacles, level_tracker, gate, inGate, mode)

        if mode == 'Classic' and level_tracker > 12:
            game_over = True

        print_game(board, snake, food, obstacles, gate, level_tracker,
                   board_edges)
        game_over = end_game(game_over, board_edges, snake_head, snake,
                             obstacles)
        time.sleep(speed)
    
    if mode == 'Classic' and level_tracker > 12:
        print("CLASSIC LEVELS FINISHED\n")
