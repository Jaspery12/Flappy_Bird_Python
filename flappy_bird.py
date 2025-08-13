import random
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
velocity_y = 0 
gravity = 0.4
score = 0
game_over = False
background_x1 = 0
background_x2 = WINDOW_WIDTH

def draw():
  global background_x1, background_x2
  
  window.blit(background_image, (background_x1,0))
  window.blit(background_image, (background_x2,0))
  window.blit(bird.img, bird)
  
  background_x1 += velocity_x
  background_x2 += velocity_x
  
  if background_x1 <= -WINDOW_WIDTH:
    background_x1 = WINDOW_WIDTH
  if background_x2 <= -WINDOW_WIDTH:
    background_x2 = WINDOW_WIDTH
  
  for pipe in pipes:
    window.blit(pipe.img, pipe)
  if game_over:
    game_over_str = "Game Over!"
    text_str = "You Scored: " + str(int(score)) 
    retry_str = "Press SPACE to retry"
    text_font = pygame.font.SysFont("Comic Sans MS", 35)
    gameover_render = text_font.render(game_over_str, True, "red")
    text_render = text_font.render(text_str, True, "white")
    retry_render = text_font.render(retry_str, True, "white")
    window.blit(gameover_render, (5, 0))
    window.blit(text_render, (5, 40))
    window.blit(retry_render, (5, 80))
    
  else:     
    text_str = "Score: " + str(int(score))  
    text_font = pygame.font.SysFont("Comic Sans MS", 35)
    text_render = text_font.render(text_str, True, "white")
    window.blit(text_render, (5,0))
    
def create_pipes():
  random_pipe_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2)
  opening_space = WINDOW_HEIGHT/4
  
  top_pipe = Pipe(top_pipe_image)
  top_pipe.y = random_pipe_y
  pipes.append(top_pipe)
  
  bottom_pipe = Pipe(bottom_pipe_image)
  bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space
  pipes.append(bottom_pipe)

def move():
  global velocity_y, score, game_over
  velocity_y += gravity
  bird.y += velocity_y
  bird.y = max(bird.y, 0)
  
  if bird.y > WINDOW_HEIGHT:
    game_over = True
    return
  
  for pipe in pipes:
    pipe.x += velocity_x
    
    if not pipe.passed and bird.x > pipe.x + pipe_width:
      score += 0.5
      pipe.passed = True
    
    if bird.colliderect(pipe):
      game_over = True
      return
    
  while len(pipes) > 0 and pipes[0].x < -pipe_width:
    pipes.pop(0)


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
      
    if event.type == create_pipes_timer and not game_over:
      create_pipes()
      
    if event.type == pygame.KEYDOWN:
      if event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
        velocity_y = -8
        
        if game_over:
          bird.y = bird_y
          pipes.clear()
          score = 0 
          game_over = False
          
  if not game_over:
    move()
    draw()
    pygame.display.update()
    clock.tick(60)
      
pygame.quit()
exit()