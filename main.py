import sys
import pygame

__author__ = 'bhansa'


def minmax(val, minval, maxval):
    return min(max(val, minval), maxval)


class Constants:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255


# Main Class of the Game, holding the game state
class Game:
    # Initializes the game
    def __init__(self):
        pygame.init()
        self.size = width, self.height = 600, 600
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Assignment: Ball Game")
        self.ball = pygame.image.load("fireball.png")
        pygame.key.set_repeat(10, 10)
        self.clk = pygame.time.Clock()
        self.loop = True
        self.x, self.y = 0, 0
        self.imgx, self.imgy = 0, 0

    # Shows a message
    def message_display(self, text):
        txt = pygame.font.Font('freesansbold.ttf', 20)
        s = txt.render(text, True, Constants.BLACK)
        sr = s.get_rect()
        sr.center = (400, 10)
        self.screen.blit(s, sr)

    # Function to run the whole game
    def run(self):
        while(self.loop):
            self._loop()

    # Runs in every game tick
    def _loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x = -5
                elif event.key == pygame.K_UP:
                    self.y = -5
                elif event.key == pygame.K_RIGHT:
                    self.x = 5
                elif event.key == pygame.K_DOWN:
                    self.y = 5
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    self.x = 0
                    self.y = 0

        self.imgx = minmax(self.imgx + self.x, 0, self.size[0] - self.ball.get_width())
        self.imgy = minmax(self.imgy + self.y, 0, self.size[1] - self.ball.get_height())
        self.screen.fill(Constants.WHITE)
        self.screen.blit(self.ball, (self.imgx, self.imgy))
        text = "x: " + str(self.imgx) + "  y: " + str(self.imgy)
        self.message_display(text)
        pygame.display.update()
        self.clk.tick(60)


# Entry point for the game
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
