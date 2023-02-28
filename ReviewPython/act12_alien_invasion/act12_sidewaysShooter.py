# Activity 12-3 Rocket

# import packages needed
import sys
import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """ Bullets """
    def __init__(self, rg_game):
        super().__init__()
        # Settings for the bullets
        
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255,255,255)

        self.screen = rg_game.screen
        
         # create a bullet
        self.bullet_rect = pygame.Rect(0, 0, self.bullet_width, 
                                       self.bullet_height)
        # set the bullet position on where the ship is
        self.bullet_rect.midright = rg_game.rect.midright

        self.x = self.bullet_rect.x



    def update(self):
        """ Move the bullet to the right """
        self.x += 1
        self.bullet_rect.x = self.x
        
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)
        

# inherits the class Sprite in the library pygame
class Rocketgame:

    def __init__(self):
        """ Initialize the variable needed """
        pygame.init()

        self.bullets = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")

        # background color
        self.bg_color = (0, 0, 0)

        # get the screen size
        self.screen_rect = self.screen.get_rect()

        # load the ship
        self.image = pygame.image.load('ReviewPython\\act12_alien_invasion\\ship.bmp')
        self.rect = self.image.get_rect() # get the rect of image

        # Start new ship at the center of the screen
        # rect is the box of the image / size 
        # screen_rect is the screen screen size
        self.rect.midleft = self.screen_rect.midleft # coordinates

        # movement flag up and down only
        self.moving_up = False
        self.moving_down = False

        self.bullets = pygame.sprite.Group()
        

       

    

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
                    elif event.key == pygame.K_SPACE:
                        self.fire_bullet()
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        # Stop ship 
                        self.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        # Stop ship 
                        self.moving_down = False
                   
            # update ship position
            self.update()

            # bullets
            self.bullets.update()

            # redraw the screen to change the bg color (black color)
            self.screen.fill(self.bg_color)
            self.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # make the most recently drawn screen visible
            pygame.display.flip()

    def fire_bullet(self):
        """ Create new bullet and store it in the group """
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)

if __name__ == "__main__":
    rg = Rocketgame()
    rg.run_game()

        