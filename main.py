import sys
import pygame
from random import *

__author__ = 'bhansa'

def minmax(val, minval, maxval):
    return min(max(val, minval), maxval)

class Constants:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

class Fireball:
    def __init__(self):
        self.vx = randint(-5, 5)    # initial velocities
        self.vy = randint(-5, 5)
        self.x = randint(0, 600)    # initial position
        self.y = randint(0, 600)
        self.fireimg = pygame.image.load("assets/fireball.png")
    
    def update(self):
        self.x = minmax(self.x + self.vx, 0, Constants.SCREEN_WIDTH - self.fireimg.get_width())
        self.y = minmax(self.y + self.vy, 0, Constants.SCREEN_HEIGHT - self.fireimg.get_height())
        
        if self.x == 0 or self.x == Constants.SCREEN_WIDTH - self.fireimg.get_width():
            self.vx *= -1   # if ball hits edge of screen reverse the velocity, to simulate bouncing off edge of screen
            
        if self.y == 0 or self.y == Constants.SCREEN_HEIGHT - self.fireimg.get_height():
            self.vy *= -1   # same in y dir

# Main Class of the Game, holding the game state
class Game:
    # Initializes the game
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Fireball")
        self.ball = pygame.image.load("assets/mario.png")
        pygame.key.set_repeat(10, 10)
        self.clk = pygame.time.Clock()
        self.loop = True
        self.x, self.y = 0, 0
        self.imgx, self.imgy = 0, 0
        
        self.timer = 0  # timer to track fireballs
        self.ball_list = []
        for x in range(6):
            self.ball_list.append(Fireball())   # list of on-screen fireballs        

    # Shows a message
    def message_display(self, text):
        txt = pygame.font.Font('freesansbold.ttf', 12)
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
            self.timer += 1
            
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
            
            if len(self.ball_list) >= 6:
                self.ball_list.pop(0)   # remove one fireball if there are more than six on-screen

        self.imgx = minmax(self.imgx + self.x, 0, self.size[0] - self.ball.get_width())
        self.imgy = minmax(self.imgy + self.y, 0, self.size[1] - self.ball.get_height())
        self.screen.fill(Constants.WHITE)
        self.screen.blit(self.ball, (self.imgx, self.imgy))
        
        for i in self.ball_list:
            i.update()  # bitblt the fireballs
            self.screen.blit(i.fireimg, (i.x, i.y))
        
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
