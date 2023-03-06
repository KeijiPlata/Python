# import the packages needed
import pygame
import sys
from pygame.sprite import Sprite

class Stars(Sprite):
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")

        # bg color
        self.bg_color = (0, 0, 0)

    def run_game(self):
        """Main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # color black bg
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    st = Stars()
    st.run_game()