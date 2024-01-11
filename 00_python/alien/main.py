# this is the alien game

# general plan of the alien game

# we control a ship that stays on the bottom center of the screen
# the player moves the ship using the arrow keys, horizontally only
# and the player shoots using the space bar
# when the game starts, aliens appers on the top of the screen and starts going down
# if the player destroys all the ships, a new fleet of aliens appers, that moves faster
# if the player ship gets hit by a alien, or if a alien hits the bottom of the screen, the player loses a live
# if the player loses all lives, it is game over

import sys
import pygame

from settings import Settings
from ship     import Ship

# random constants

WINDOW_TITLE = "Alien Invasion"
ASSET_NOT_FIND_ERROR = "Error: game assets not found. Make sure to get them and put it on the assets folder."

# overall class that manages game assets and behavior
class AlienInvasion:
    def __init__(self):
        #initializes the game and create game resources
        pygame.init()

        # creates an instance of the class Clock
        self.clock = pygame.time.Clock()

        # imports the settings class
        self.settings = Settings()

        # this is called "surface"
        self.screen = pygame.display.set_mode((self.settings.screen_widht, self.settings.screen_height))

        # this sets the window title
        pygame.display.set_caption(WINDOW_TITLE)

        # set the background color
        self.bg_color = (self.settings.bg_color)

        # imports the ship class
        self.ship = Ship(self)

    # starts the main loop of the game
    def run_game(self):

        while True:
            # watch for keyboard and mouse input aka a event loop that listen to events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # this is the event loop checking for when the user quits (aka closes the screen)
                    sys.exit()

            # redraw the screen on each time loop iteration
            self.screen.fill(self.settings.bg_color)

            # imports the ship class
            self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()

            # controls the frame rate
            self.clock.tick(self.settings.refrash_rate)


if __name__ == '__main__':
    # makes a game instance
    ai = AlienInvasion()

    # runs the game
    ai.run_game()


