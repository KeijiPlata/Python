# import packages needed
import pygame
import sys
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Create a fleet of raindrops"""
    def __init__(self, raindropGame):
        super().__init__()

        # load the raindrop image
        self.screen = raindropGame.screen
        path = 'ReviewPython\\act13_raindrops\\raindrops.bmp'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        # start each new raindrop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position
        self.y = float(self.rect.y)
        self.raindrop_speed = 0.1

    def update(self):
        """move the raindrops down"""
        self.y += self.raindrop_speed
        self.rect.y = self.y

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

        # create raindrop group
        self.raindrops = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """Create fleet of raindrops"""
        raindrop = Raindrop(self)
        
        raindrops_width, raindrops_height = raindrop.rect.size

        # compute for the available space
        available_space_x = self.screen_width - raindrops_width# full width
        available_space_y = self.screen_height
        number_rows = available_space_y // (2 * raindrops_height)
        number_raindorps_x = available_space_x // (2 * raindrops_width)

        for row in range(number_rows):    
            for raindropsNum in range(number_raindorps_x):
                raindrop = Raindrop(self)
                raindrops_width, raindrops_height = raindrop.rect.size
                raindrop.y = 2* raindrops_height * row
                raindrop.rect.y = raindrop.y
                raindrop.rect.x =  raindrops_width + 2 * raindrops_width * raindropsNum
                self.raindrops.add(raindrop)

    def run_game(self):
        """main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # color black bg
            self.screen.fill(self.bg_color)

            # draw the raindrops
            self.raindrops.draw(self.screen)

            # movement 
            self.raindrops.update()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    rd = Rain()
    rd.run_game()