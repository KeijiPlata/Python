# import packages needed
import pygame
import sys
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Create a fleet of raindrops"""
    def __init__(self, raindropGame):
        super.__init__()

class Rain():
    """Manage the raindrops"""
    def __init__(self):
        """Initializing variables"""
        pygame.init()

        # set screen size
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("Rain")

        # bg color
        self.bg_color = (0, 0, 0)

    def run_game(self):
        """main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    rd = Rain()
    rd.run_game()