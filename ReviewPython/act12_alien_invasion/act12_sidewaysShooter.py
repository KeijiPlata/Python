# Activity 12-3 Rocket

# import packages needed
import sys
import pygame

class Rocketgame:
    """ A game where the rocket will spawn to center and move around using
    arrow keys """

    def __init__(self):
        """ Initialize the variable needed """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")

        # background color
        self.bg_color = (0, 0, 0)

        # get the screen size
        self.screen_rect = self.screen.get_rect()

        # load the ship
        self.image = pygame.image.load('ReviewPython\\act12_alien_invasion\\ship.bmp')

        # rotates the image
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect() # get the rect of image

        # Start new ship at the center of the screen
        # rect is the box of the image / size 
        # screen_rect is the screen screen size
        self.rect.centery = self.screen_rect.centery # coordinates

        # movement flag up and down only
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Move the ship to the left
                        self.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        # Move the ship to the left
                        self.moving_down = True
                    elif event.key == pygame.K_q:
                        # if user press q, it will quit the game
                        sys.exit()
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        # Stop ship 
                        self.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        # Stop ship 
                        self.moving_down = False
                   

            self.update()
            # redraw the screen to change the bg color (black color)
            self.screen.fill(self.bg_color)
            self.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    rg = Rocketgame()
    rg.run_game()

        