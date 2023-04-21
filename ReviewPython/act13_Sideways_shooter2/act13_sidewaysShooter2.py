# Activity 12-3 Rocket

# import packages needed
import sys
import pygame
from pygame.sprite import Sprite
from time import sleep

class GameStats:
    """track statistics"""

    def __init__(self, rg_game):
        """initialize variables"""
        self.reset_stats()

        # game state
        self.game_active = True

    def reset_stats(self):
        """reset"""
        self.ship_left = 3
        

class Alien(Sprite):
    """Aliens"""
    def __init__(self, rg_game):
        """Initizalize the alien"""
        super().__init__()
        self.screen = rg_game.screen

        # load the image of alien
        self.image = pygame.image.load('ReviewPython\\act13_Sideways_shooter2\\alien.bmp')
        self.rect = self.image.get_rect()

        # alien position
        self.rect.x = 1200 - self.rect.width
        self.rect.y = self.rect.height

        # store aliean horizontal position
        self.x = self.rect.x
        self.y = self.rect.y

        # alien movement speed
        self.alien_speed = 1

    def update(self):
        """Move the alien up and down then to the left"""
        self.x -= self.alien_speed
        self.rect.x = float(self.x)


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
        self.rect = pygame.Rect(0, 0, self.bullet_width, 
                                       self.bullet_height)
        # set the bullet position on where the ship is
        self.rect.midright = rg_game.ship.rect.midright

        self.x = self.rect.x

    def update(self):
        """ Move the bullet to the right """
        self.x += 1
        self.rect.x = self.x
        
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

class Ship:
    """ship"""
    def __init__(self, rg_game):
        """initialize variables"""
        self.screen = rg_game.screen
        self.screen_rect = rg_game.screen.get_rect()

        # load the ship
        self.image = pygame.image.load('ReviewPython\\act13_Sideways_shooter2\\ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect() # get the rect of image

        # Start new ship at the center of the screen
        # rect is the box of the image / size 
        # screen_rect is the screen screen size
        self.rect.midleft = self.screen_rect.midleft # coordinates

        # movement flag up and down only
        self.moving_up = False
        self.moving_down = False

        self.x = self.rect.x

    
    def update(self):
        """movements"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1


    def blitme(self):
        """draw the image to the screen"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship"""
        self.rect.midleft = self.screen_rect.midleft

        
            

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

        # initialize the ship
        self.ship = Ship(self)

        # initialize the stats
        self.stats = GameStats(self)

        # group for bullets
        self.bullets = pygame.sprite.Group()

        # group for aliens
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

    def _check_aliens_left(self):
        """check if the alien is in the right side of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.left < self.screen.get_rect().left:
                self._ship_hit()
                break


    def _update_aliens(self):
        """Update the position of rows"""
        self.aliens.update()

        # look for the alien ship colliesions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_left()

    def _create_fleet(self):
        alien = Alien(self)
        alien_height = alien.rect.height
        available_y = 800 - alien_height
        number_y = available_y // alien_height
        
        # create row
        for rowNumber in range(2):
            for alienNumber in range(number_y):
                alien = Alien(self)
                alien_height = alien.rect.height
                alien_width = alien.rect.width
                alien.x = 900 + 2 * alien_width * rowNumber
                alien.rect.x = alien.x
                alien.y = alien_height + alien_height * alienNumber
                alien.rect.y = alien.y
                self.aliens.add(alien)


    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Move the ship to the left
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        # Move the ship to the left
                        self.ship.moving_down = True
                    elif event.key == pygame.K_q:
                        # if user press q, it will quit the game
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self.fire_bullet()
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        # Stop ship 
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        # Stop ship 
                        self.ship.moving_down = False
            
            if self.stats.game_active:
                # update ship position
                self.ship.update()

                # bullets
                self.bullets.update()

                if not self.aliens:
                # destroy bullets and create new fleet
                    self.bullets.empty()
                    self._create_fleet()

                collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                    True, True)

                # update movement alien
                self._update_aliens()

            # redraw the screen to change the bg color (black color)
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

            # make the most recently drawn screen visible
            pygame.display.flip()

    def fire_bullet(self):
        """ Create new bullet and store it in the group """
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)

    def _ship_hit(self):
        """ Respond when the ship is hit"""

        if self.stats.ship_left > 0:
            # decrement life
            self.stats.ship_left -= 1

            # get rid of any bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False
    


if __name__ == "__main__":
    rg = Rocketgame()
    rg.run_game()

        