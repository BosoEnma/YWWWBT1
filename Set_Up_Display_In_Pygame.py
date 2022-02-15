import pygame
pygame.init()
#ScreenResolution
screen = pygame.display.set_mode((1080,720))
#FPS
clock = pygame.time.get_ticks()
#While loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
      
#updates the screen
pygame.display.update(screen)
clock.tick(30)
