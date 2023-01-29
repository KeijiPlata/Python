# Activity 12-2 Game Character

import pygame
import sys

class BlueSky:
    """Make the pygame window blue acitivity"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        # screen/form size
        self.screen = pygame.display.set_mode((1200, 800))

        # form name
        pygame.display.set_caption("Blue Sky")

        # change bg color
        self.bg_color = (173, 216, 230) 

        # get the screen size
        self.screen_rect = self.screen.get_rect()

        # image
        self.image = pygame.image.load('ReviewPython\\act12_alien_invasion\\mario.bmp')

        # get the image rectangle
        self.rect = self.image.get_rect()

        # put the ship to the midbottom
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw the ship at ist current location"""
        self.screen.blit(self.image, self.rect)

    def run_game(self):
         """Start the main loop for the game"""
         while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen
            self.screen.fill(self.bg_color)

            # draw theimage to the screen
            self.blitme()

            # make the new screen vvisible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance
    bsky = BlueSky()
    bsky.run_game()

        