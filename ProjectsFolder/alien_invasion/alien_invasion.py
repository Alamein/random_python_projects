# import sys :already imported in the module game_functions

import pygame
from pygame.sprite import Group
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

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        #  Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

        gf.update_aliens(aliens)

        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()

        # # Make the most recently drawn screen visible.
        # pygame.display.flip()

run_game()