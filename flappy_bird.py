import pygame
from sys import exit 

WINDOW_WIDTH = 360  
WINDOW_HEIGHT = 640

background_image = pygame.image.load("flappybirdbg.png")

def draw():
  window.blit(background_image, (0,0))

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
  
  draw()
  pygame.display.update()
  clock.tick(60)
      
pygame.quit()
exit()