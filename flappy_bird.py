import pygame
from sys import exit 

#Background
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

#Pipes
pipe_x = WINDOW_WIDTH
pipe_y = 0
pipe_width = 64
pipe_height = 512

class Pipe(pygame.Rect):
  def __init__(self, img):
    pygame.Rect.__init__(self, pipe_x, pipe_y, pipe_width, pipe_height)
    self.img = img
    self.passed = False

#Images 
background_image = pygame.image.load("flappybirdbg.png")
bird_image = pygame.image.load("flappybird.png")
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
icon = pygame.display.set_icon(bird_image)
top_pipe_image = pygame.image.load("toppipe.png")
top_pipe_image = pygame.transform.scale(top_pipe_image,(pipe_width, pipe_height))
bottom_pipe_image = pygame.image.load("bottompipe.png")
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))


#Logic
bird = Bird(bird_image)
pipes = []
velocity_x = -2

def draw():
  window.blit(background_image, (0,0))
  window.blit(bird.img, bird)
  
  for pipe in pipes:
    window.blit(pipe.img, pipe)
  
def create_pipes():
  top_pipe = Pipe(top_pipe_image)
  pipes.append(top_pipe)
  
def move():
  for pipe in pipes:
    pipe.x += velocity_x


#Window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1750)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
      
    if event.type == create_pipes_timer:
      create_pipes()
  
  move()
  draw()
  pygame.display.update()
  clock.tick(60)
      
pygame.quit()
exit()