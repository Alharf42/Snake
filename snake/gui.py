import pygame
import readchar
import sys
from game_logic import (
    start_game, execute_game_logic, end_game, board, board_edges
)

# Pygame initialization
pygame.init()

# Global static variables for size and colors
GRID_SIZE = 30
COLOR_BG = (0, 0, 0)
COLOR_DARK = (43, 51, 25)
COLOR_SNAKE = (57, 255, 20)
COLOR_FOOD = (247, 33, 25)
COLOR_WALLS = (128, 128, 128)
COLOR_GATE = (255, 255, 255)

# Set font
font = pygame.font.SysFont("monospace", 35)
font_small = pygame.font.SysFont("monospace", 25)


# The screen target is passed into the drawing helper directly
def draw_grid_object(screen, coords, color):
    # Helper to map console logic (row, col) array matrix to pygame (x, y) screen coordinates
    row, col = coords[0], coords[1]
    rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE-1, GRID_SIZE-1)
    pygame.draw.rect(screen, color, rect)


def draw_grid_object_circle(screen, coords, color):
    #Helper to map the console logic (row, col) array matrix to pygame (x, y) screen coordinates
    row, col = coords[0], coords[1]
    
    # Calculate base grid positions
    top_left_x = col * GRID_SIZE
    top_left_y = row * GRID_SIZE
    # Find the exact center point of the cell for the circle
    center_x = top_left_x + GRID_SIZE // 2
    center_y = top_left_y + GRID_SIZE // 2
    # Radius is slightly smaller than half grid size so circles look cleanly separated
    radius = (GRID_SIZE // 2) - 1
    pygame.draw.circle(screen, color, (center_x, center_y), radius)


def endLevels(screen):
    
    while True:
        screen.fill(COLOR_BG)
        
        text = font.render("Classic levels finished", True, COLOR_GATE)
        text2 = font.render("Press any key to continue...", True, COLOR_GATE)
        
        screen.blit(text, (20, 30))
        screen.blit(text2, (20, 60))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()


def startUpMenu(screen):
    # Mode and speed variables
    selected_speed = 200  # 150 350
    selected_mode = 'Regular'
    selected_theme = 'Default'

    while True:
        
        screen.fill(COLOR_BG)
        mouse = pygame.mouse.get_pos()

        play_button = pygame.Rect(230, 80, 140, 50)
        quit_button = pygame.Rect(230, 150, 140, 50)
        
        # Mode buttons
        regular_button = pygame.Rect(45, 290, 150, 50)
        classic_button = pygame.Rect(225, 290, 150, 50)
        random_button = pygame.Rect(405, 290, 150, 50)
        
        # Speed buttons
        slow_button = pygame.Rect(45, 430, 150, 50)
        medium_button = pygame.Rect(225, 430, 150, 50)
        fast_button = pygame.Rect(405, 430, 150, 50)
        
        # Theme selector buttons
        defaultTheme_button = pygame.Rect(45, 550, 150, 50)
        retroTheme_button = pygame.Rect(225, 550, 150, 50)
        cyberpunkTheme_button = pygame.Rect(405, 550, 150, 50)

        pygame.draw.rect(screen, COLOR_WALLS if play_button.collidepoint(mouse) else COLOR_DARK, play_button)
        pygame.draw.rect(screen, COLOR_WALLS if quit_button.collidepoint(mouse) else COLOR_DARK, quit_button)
        
        # Draw game modes
        pygame.draw.rect(screen, COLOR_SNAKE if selected_mode == 'Regular' else (COLOR_WALLS if regular_button.collidepoint(mouse) else COLOR_DARK), regular_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_mode == 'Classic' else (COLOR_WALLS if classic_button.collidepoint(mouse) else COLOR_DARK), classic_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_mode == 'Random'  else (COLOR_WALLS if random_button.collidepoint(mouse) else COLOR_DARK), random_button)
        # Draw speeds
        pygame.draw.rect(screen, COLOR_SNAKE if selected_speed == 350 else (COLOR_WALLS if slow_button.collidepoint(mouse) else COLOR_DARK), slow_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_speed == 200 else (COLOR_WALLS if medium_button.collidepoint(mouse) else COLOR_DARK), medium_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_speed == 150 else (COLOR_WALLS if fast_button.collidepoint(mouse) else COLOR_DARK), fast_button)
        # Draw theme selector
        pygame.draw.rect(screen, COLOR_SNAKE if selected_theme == 'Default' else (COLOR_WALLS if defaultTheme_button.collidepoint(mouse) else COLOR_DARK), defaultTheme_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_theme == 'Retro' else (COLOR_WALLS if retroTheme_button.collidepoint(mouse) else COLOR_DARK), retroTheme_button)
        pygame.draw.rect(screen, COLOR_SNAKE if selected_theme == 'Cyberpunk' else (COLOR_WALLS if cyberpunkTheme_button.collidepoint(mouse) else COLOR_DARK), cyberpunkTheme_button)
        
        play_text = font.render("Play", True, COLOR_GATE)
        quit_text = font.render("Quit", True, COLOR_GATE)
        
        # Mode text
        regular_text = font.render("Regular", True, COLOR_GATE)
        classic_text = font.render("Classic", True, COLOR_GATE)
        random_text = font.render("Random", True, COLOR_GATE)
        # Speed text
        slow_text = font.render("Slow", True, COLOR_GATE)
        medium_text = font.render("Medium", True, COLOR_GATE)
        fast_text = font.render("Fast", True, COLOR_GATE)
        
        # Theme text
        default_text = font.render("Default", True, COLOR_GATE)
        retro_text = font.render("Retro", True, COLOR_GATE)
        cyberpunk_text = font.render("Cyber", True, COLOR_GATE)
        
        # Section header labels
        mode_label = font.render("SELECT MODE", True, COLOR_GATE)
        speed_label = font.render("SELECT SPEED", True, COLOR_GATE)
        theme_label = font. render("SELECT THEME", True, COLOR_GATE)
        
        # Main actions, play and quit
        screen.blit(play_text, (260, 85))
        screen.blit(quit_text, (260, 155))

        # Labels of sections
        screen.blit(mode_label, (165, 235))
        screen.blit(speed_label, (165, 375))
        screen.blit(theme_label, (165, 500))

        # Mode row elements
        screen.blit(regular_text, (50, 295))
        screen.blit(classic_text, (227, 295))
        screen.blit(random_text, (418, 295))

        # Speed row elements
        screen.blit(slow_text, (80, 435))
        screen.blit(medium_text, (240, 435))
        screen.blit(fast_text, (445, 435))
        
        # Theme row elements
        screen.blit(default_text, (50, 555))
        screen.blit(retro_text, (250, 555))
        screen.blit(cyberpunk_text, (430, 555))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # Mode button values
                    if regular_button.collidepoint(mouse):
                        selected_mode = 'Regular'
                    elif classic_button.collidepoint(mouse):
                        selected_mode = 'Classic'
                    elif random_button.collidepoint(mouse):
                        selected_mode = 'Random'

                    # Speed button values
                    if slow_button.collidepoint(mouse):
                        selected_speed = 350
                    elif medium_button.collidepoint(mouse):
                        selected_speed = 200
                    elif fast_button.collidepoint(mouse):
                        selected_speed = 150

                    # Theme button values
                    if defaultTheme_button.collidepoint(mouse):
                        selected_theme = 'Default'
                    elif retroTheme_button.collidepoint(mouse):
                        selected_theme = 'Retro'
                    elif cyberpunkTheme_button.collidepoint(mouse):
                        selected_theme = 'Cyberpunk'
                    
                    # Play and start game
                    if play_button.collidepoint(mouse):
                        # Return selected values
                        # Higher delay = slower game loop speed
                        return selected_mode, selected_speed, selected_theme

                    # Quit
                    if quit_button.collidepoint(mouse):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


def game():
    
    # Calculate screen proportions based on board matrix dimension
    WINDOW_SIZE = len(board) * GRID_SIZE 
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE+30))
    pygame.display.set_caption("Snake - Pygame Edition")
    clock = pygame.time.Clock()
    
    # Start up menu
    # Choose speed and mode
    mode, speed, theme = startUpMenu(screen)

    # Define game state logic variables
    game_over = False
    not_eaten = 0
    obstacles = []
    level_tracker = 0
    gate = []
    inGate = False
    snake_head, snake, food = start_game(board, obstacles)
    
    # Snake starts moving right using exact readchar variables from console version
    direction = readchar.key.RIGHT
    next_direction = direction

    # Clock timer variables
    SNAKE_STEP_DELAY = speed
    last_move_time = pygame.time.get_ticks()

    # Game loop
    while not game_over:
        current_time = pygame.time.get_ticks()

        # Keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != readchar.key.RIGHT:
                    next_direction = readchar.key.LEFT
                elif event.key == pygame.K_RIGHT and direction != readchar.key.LEFT:
                    next_direction = readchar.key.RIGHT
                elif event.key == pygame.K_UP and direction != readchar.key.DOWN:
                    next_direction = readchar.key.UP
                elif event.key == pygame.K_DOWN and direction != readchar.key.UP:
                    next_direction = readchar.key.DOWN
                elif event.key == pygame.K_p:
                    pygame.time.wait(2000000)
                    

        # Game logic
        if current_time - last_move_time >= SNAKE_STEP_DELAY:
            direction = next_direction  
            
            snake_head, snake, food, not_eaten, obstacles, level_tracker, gate, inGate = execute_game_logic(snake_head, snake, food, not_eaten, direction, obstacles, level_tracker, gate, inGate, mode)
                
            if mode == 'Classic' and level_tracker > 12:
                game_over = True
            
            game_over = end_game(game_over, board_edges, snake_head, snake, obstacles)

            last_move_time = current_time

        # Environment
        
        bgColor = COLOR_BG
        darkColor = COLOR_DARK
        snakeColor = COLOR_SNAKE
        foodColor = COLOR_FOOD
        wallsColor = COLOR_WALLS
        gateColor = COLOR_GATE
        
        if theme == "Default":
            bgColor = COLOR_BG
            darkColor = COLOR_DARK
            snakeColor = COLOR_SNAKE
            foodColor = COLOR_FOOD
            wallsColor = COLOR_WALLS
            gateColor = COLOR_GATE
        elif theme == "Retro":
            bgColor = (87, 128, 59)
            lcd_grid_color = (78, 115, 53)
            gateColor = (15, 35, 10)

            # Lighter grid
            darkColor = (15, 35, 10)     
            snakeColor = (15, 35, 10)     
            foodColor = (15, 35, 10)     
            wallsColor = (15, 35, 10)

        elif theme == "Cyberpunk":
            bgColor = (26, 15, 36)
            lcd_grid_color = (43, 26, 59)
            gateColor = (252, 245, 28)

            # Lighter grid
            darkColor = (255, 0, 127)
            snakeColor = (229, 18, 252)
            foodColor = (252, 245, 28)
            wallsColor = (0, 139, 252)
        
        screen.fill(bgColor)
        
        if theme == "Retro" or theme == 'Cyberpunk':
            for r in range(len(board)):
                for c in range(len(board[0])):
                    rect = pygame.Rect(c * GRID_SIZE + 1, r * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2)
                    pygame.draw.rect(screen, lcd_grid_color, rect, 1)

        # Draw the current level and snake length
        textLine = font_small.render("Current level: " + str(level_tracker), True, gateColor)
        textLine2 = font_small.render("Snake size: " + str(len(snake)), True, gateColor)
        
        screen.blit(textLine, (5, 600))
        screen.blit(textLine2, (370, 600))
        
        # Draw generated board walls
        for wall in board_edges:
            draw_grid_object(screen, wall, wallsColor)

        # Draw target food
        draw_grid_object_circle(screen, food, foodColor)
        
        # Draw gate
        if gate:
            draw_grid_object(screen, gate, gateColor)

        # Draw snake
        for segment in snake:
            draw_grid_object_circle(screen, segment, snakeColor)
        
        # Draw obstacles
        for segment in obstacles:
            if segment[0] < 20:
                draw_grid_object(screen, segment, wallsColor)

        pygame.display.flip()
        clock.tick(60)  
    # New window for finished levels
    if mode == 'Classic' and level_tracker > 12:
        endLevels(screen)
    # Keep window open briefly at game over
    pygame.time.wait(2000)
    pygame.quit()
