import pygame

# pygame treats all 2d game art as rects, even when they are not

class Ship:
    def __init__(self, ai_game):

        # initializes the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # loads the ship and get its rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):

        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)


