# The main module, here the game boots up and
# the main environment is chosen
from console_loop import console_game
from gui import game


def gui_available():
    try:
        import pygame
        pygame.display.init()
        pygame.display.set_mode((1, 1))
        pygame.display.quit()
        return True
    except:
        return False


if gui_available():
    # start gui version
    #console_game()
    game()
else:
    print("GUI not available, running console version.")
    # run_console_game()
    console_game()