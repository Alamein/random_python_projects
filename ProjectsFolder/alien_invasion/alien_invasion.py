# import sys :already imported in the module game_functions

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Inversion")

    # Set the background color.
    # bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:

        #  Watch for keyboard and mouse events.
        gf.check_events(ship)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        ship.update()

        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()

        # # Make the most recently drawn screen visible.
        # pygame.display.flip()

run_game()





# # import sys :already imported in the module game_functions

# import pygame
# from settings import Settings
# from ship import Ship
# import game_functions as gf

# def run_game():
#     # Initialize game and create a screen object.
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Inversion")

#     # Set the background color.
#     # bg_color = (230, 230, 230)

#     # Make a ship
#     ship = Ship(ai_settings, screen)

#     # Start the main loop for the game.
#     while True:

#         #  Watch for keyboard and mouse events.
#         gf.check_events(ship)
#         # for event in pygame.event.get():
#         #     if event.type == pygame.QUIT:
#         #         sys.exit()

#         ship.update()

#         # Redraw the screen during each pass through the loop.
#         gf.update_screen(ai_settings, screen, ship)
#         # screen.fill(ai_settings.bg_color)
#         # ship.blitme()

#         # # Make the most recently drawn screen visible.
#         # pygame.display.flip()

# run_game()