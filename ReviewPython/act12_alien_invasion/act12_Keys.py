# Activity 12-3 Rocket

# import packages needed
import sys
import pygame

class Keygame:
    """ A game where the rocket will spawn to center and move around using
    arrow keys """

    def __init__(self):
        """ Initialize the variable needed """
        pygame.init()

        # set the screen size
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Print Keys")

        # background color
        self.bg_color = (40, 160, 200)

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # prints the letter in console
                    print(event.unicode)
                   
            # redraw the screen to change the bg color (blue)
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    kg = Keygame()
    kg.run_game()

        