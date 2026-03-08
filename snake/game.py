import readchar
import time
import msvcrt
import random
import numpy as np

# structure of the game
# board-2D grid, snake-list of tuples(coordinates(indeces) of the grid(board)), food just one tuple


# create board
board = np.zeros((20, 20), dtype=int)


# create snake size 1x1 at the beginning
snake = list((x, y) for x in range(1, 2) for y in range(1, 2))
# add conditions for snake-can grow in length only in one direction
# grows in length only by one and only when he eats food

# snake's head is the first coordinate which can consume, crash,
#  and beggins a movement and direction change
snake_head = snake[0]

# edges are on (1,y), (x,1), (20, y), (x, 20) coordinates
board_edges = {
    *[(x, 0) for x in range(0, len(board) - 1)],
    *[(x, len(board)-1) for x in range(0, len(board) - 1)],
    *[(0, y) for y in range(0, len(board[0]) - 1)],
    *[(len(board[0]-1), y) for y in range(0, len(board[0]) - 1)]
}


# coordinates of food chosen randomely within the board size

# at start of the game set the size of the board


def start_game(board):
    # ask the size of the board-for now 20
    # put snake in the middle-start with size 1x1 - snake head
    snake_head = (10, 10)
    snake = [snake_head]
    return snake_head, snake, spawn_food(board)

# win a game when snake too big? in the end snake will get to next level trough gate which shows up after a certain length of the snake
def end_game(end_game, board_edges, snake_head, snake):
    # game ends when snake will crash to himself or end of the board
    # fi snake crashes return true else false

    if (snake_head in board_edges):
        end_game = True
        print("GAME OVER")

    if (snake_head in snake[1:]):
        end_game = True
        print("GAME OVER")

    return end_game


def spawn_food(board):
    return (random.randint(0+1, len(board)-1-1), random.randint(0+1, len(board)-1-1))


def update_snake_position(snake, snake_head):

    # last is pre last, pre last is pre pre last etc until head, which is already set
    # and shoudnt change
    # list is python is a dynamic array with indexes
    
    # new algo!!!! insert new head at the beggining and pop the end
    # this way the intended shift happens without any loop

    #for i in range(len(snake)-1, 2, -1):
    #   snake[i] = snake[i-1]
    #snake[0] = snake_head
    snake.insert(0, snake_head)
    snake.pop(-1)
    return snake


def snake_move(snake, direction):
    if direction == readchar.key.LEFT:
        # move left
        # snake[0] =
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

# def shorten_snake_after_not_eating_for_a_while()

# def make_food_dissapear_after_not_being_eaten_for_a_while()
# keep attention to spwaining new food after previous one wasnt eaten

def get_optional_key():
    if msvcrt.kbhit():
        return readchar.readkey()
    else: 
        return None
    
    
def game():
    
    # need to set physical time for each time step
    game_over = False
    direction = readchar.key.RIGHT
    snake_head, snake, food = start_game(board)
    not_eaten = 0
    print_game(board, snake, food)
    while game_over is not True:
        
        # ask direction to user-give optional
        # user has only a limited time to insert direction, otherwise snake will move straight
        # that time is equal to the time of timestep
        # ask for a given time whether user hit a key
        # for i in range(20):
        key = get_optional_key()
        if key is not None:
            direction = key
        # snake moves
        snake_head = snake_move(snake, direction)
        if len(snake) > 1:
            snake = update_snake_position(snake, snake_head)
        else:
            snake[0] = snake_head

        if (snake_head == food):
            # increase size of snake
            # TODO append in proper direction, right now its diagonal
            snake.append((snake[-1][0] + 1, snake[-1][1] + 1))
            # spawn new food
            food = spawn_food(board)
            not_eaten = 0

        # snake does not die of hunger
        if (not_eaten == 17 and len(snake) > 1):
            # loose the tail
            snake.pop(-1)

        print_game(board, snake, food)
        not_eaten += 1
        game_over = end_game(game_over, board_edges, snake_head, snake)
        time.sleep(2)


def print_game(board, snake, food):
    # when empty board .
    # when food *
    # when snake o
    
    for i in range(0, len(board)-1):
        for j in range(0, len(board[1])-1):
            if (i, j) in snake:
                print("o", end="")
            elif (i, j) == food:
                print("*", end="")
            else:
                print(" . ", end="")
        print()
    print()
