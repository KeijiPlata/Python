# import the packages needed
import pygame
import sys
from pygame.sprite import Sprite

class Stars(Sprite):
    def __init__(self, stgame):
        """Initialize the star position"""
        super().__init__() # inherits sprite library
        self.screen = stgame.screen # get the screen of the game
        # import the image star
        self.image = pygame.image.load('ReviewPython\\act13_stars\\stars.bmp')
        self.rect = self.image.get_rect()

        # stars starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien exact location
        self.x = self.rect.x
        
class StarsGame():
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")

        # bg color
        self.bg_color = (0, 0, 0)

        # create aliens
        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        stars = Stars(self)
        self.stars.add(stars)

    def run_game(self):
        """Main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # color black bg
            self.screen.fill(self.bg_color)

            # draw the stars
            self.stars.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':
    st = StarsGame()
    st.run_game()