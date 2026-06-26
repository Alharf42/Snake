import random
import readchar
import numpy as np
from levels import generate_levels

# Structure of the game
# Board-2D grid, snake-list of tuples(coordinates(indeces) of the grid(board)), food just one tuple


# Create board
board = np.zeros((20, 20), dtype=int)


# Create snake size 1x1 at the beginning
snake = list((x, y) for x in range(1, 2) for y in range(1, 2))
# Add conditions for snake-can grow in length only in one direction
# grows in length only by one and only when he eats food

# Snake's head is the first coordinate which can consume, crash,
# and beggins a movement and direction change
snake_head = snake[0]

# edges are on (1,y), (x,1), (20, y), (x, 20) coordinates
board_edges = {
    *[(x, 0) for x in range(0, len(board))],
    *[(x, len(board)-1) for x in range(0, len(board))],
    *[(0, y) for y in range(0, len(board[0]))],
    *[(len(board[0])-1, y) for y in range(0, len(board[0]))]
}


# Coordinates of food chosen randomly within the board size

# At start of the game set the size of the board


def start_game(board, obstacles):
    # Put snake in the middle, start with size 1x1, thats the snake's head
    snake_head = (10, 10)
    snake = [snake_head]
    return snake_head, snake, spawn_food(board, obstacles)


# In the end snake will get to next level trough gate which shows up after
# a certain length of the snake
def end_game(end_game, board_edges, snake_head, snake, obstacles):
    # Game ends when snake will crash to himself or end of the board
    # fi snake crashes return true else false

    if (snake_head in board_edges):
        end_game = True
        print("GAME OVER")

    if (snake_head in snake[1:]):
        end_game = True
        print("GAME OVER")

    if (snake_head in obstacles):
        end_game = True
        print("GAME OVER")

    return end_game


def spawn_food(board, obstacles):
    inObstacle = True
    food = (0, 0)
    while inObstacle:
        food = (random.randint(0+1, len(board)-1-1), random.randint(0+1, len(board)-1-1))
        if food not in obstacles:
            inObstacle = False
    return food


def update_snake_position(snake, snake_head):

    # Insert new head at the start and pop the end
    # This way the intended shift happens without any loop

    snake.insert(0, snake_head)
    snake.pop(-1)
    return snake


def snake_move(snake, direction):
    if direction == readchar.key.LEFT:
        # move left
        return (snake[0][0], snake[0][1] - 1)
    elif direction == readchar.key.RIGHT:
        # move right
        return (snake[0][0], snake[0][1] + 1)
    elif direction == readchar.key.UP:
        # move top
        return (snake[0][0] - 1, snake[0][1])
    elif direction == readchar.key.DOWN:
        # move down
        return (snake[0][0] + 1, snake[0][1])


def execute_game_logic(snake_head, snake, food, not_eaten, direction, obstacles, levels_tracker, gate, inGate, mode):
    ate_food = False
    obstacles = generate_levels(levels_tracker, obstacles, mode)


    # If snake reaches this length a gate to next level is spawned
    if (len(snake) >= 5 and not inGate):
    # Generate gate
        gate = spawn_food(board, obstacles)
        inGate = True
    # When snake touches the gate
    # Increase the number of levels reached
    # Assign gate to null
    # Return snake to the start at 1 length
    # Create new obstacles based on levels_tracker
    # And spawn new food
    if gate in snake:
        levels_tracker = levels_tracker + 1
        gate = []
        snake = [(10, 10)]
        snake_head = (10, 10)

    # New obstacles based on that
        obstacles = generate_levels(levels_tracker, [], mode)
        food = spawn_food(board, obstacles)
        inGate = False
    
    # Snake grows when he eats food
    if (snake_head == food):
        # Increase size of snake
        old_tail = snake[-1]
        snake.append(old_tail)
        # Spawn new food
        food = spawn_food(board, obstacles)
        not_eaten = 0
        ate_food = True
        
    # Snake moves
    snake_head = snake_move(snake, direction)
    if len(snake) > 1:
        snake = update_snake_position(snake, snake_head)
    else:
        snake[0] = snake_head
    
    # Snake does not die of hunger
    if not ate_food:
        if (not_eaten == 30 and len(snake) > 1):
            # Loose the tail
            snake.pop(-1)
            not_eaten = 0
        not_eaten += 1
    
    return snake_head, snake, food, not_eaten, obstacles, levels_tracker, gate, inGate
