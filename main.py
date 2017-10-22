__author__ = 'bhansa'
import sys, pygame

pygame.init()
size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Assignment: Ball Game")
ball = pygame.image.load("fireball.png")
pygame.key.set_repeat(10, 10)
clk = pygame.time.Clock()
loop = True
x, y = 0, 0
imgx, imgy = 0, 0


def message_display(text):
    txt = pygame.font.Font('freesansbold.ttf', 20)
    s = txt.render(text, True, black)
    sr = s.get_rect()
    sr.center = (400, 10)
    screen.blit(s, sr)


while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -5
            elif event.key == pygame.K_UP:
                y = -5
            elif event.key == pygame.K_RIGHT:
                x = 5
            elif event.key == pygame.K_DOWN:
                y = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x = 0
                y = 0
    imgx += x
    imgy += y
    screen.fill(white)
    screen.blit(ball, (imgx, imgy))
    text = "x: " + str(imgx) + "  y: " + str(imgy)
    message_display(text)
    pygame.display.update()
    clk.tick(60)
# By Bharat Saraswat
