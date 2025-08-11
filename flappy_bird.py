import pygame
from sys import exit 

WINDOW_WIDTH = 360  
WINDOW_HEIGHT = 640

#Bird
bird_x = WINDOW_WIDTH/8
bird_y = WINDOW_HEIGHT/2
bird_width = 34  #17:12
bird_height = 24

class Bird(pygame.Rect):
  def __init__(self, img):
    pygame.Rect.__init__(self, bird_x, bird_y, bird_width, bird_height)
    self.img = img 

#Images 
background_image = pygame.image.load("flappybirdbg.png")
bird_image = pygame.image.load("flappybird.png")
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
icon = pygame.display.set_icon(bird_image)

#Logic
bird = Bird(bird_image)

def draw():
  window.blit(background_image, (0,0))
  window.blit(bird.img, bird)

#Window
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