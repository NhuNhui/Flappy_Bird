# add library pygame
import pygame
pygame.init

#caption
pygame.display.set_caption("Plappy Bird")

#icon
icon = pygame.image.load(r'FileGame\assets\icon_flappybird.jpg')
pygame.display.set_icon(icon)

#backgound
bg = pygame.image.load(r'FileGame\assets\background-night.png')
bg = pygame.transform.scale2x(bg)

floor = pygame.image.load(r'FileGame\assets\floor.png')
floor = pygame.transform.scale2x(floor)

x_floor = 0

#create screen game
screen = pygame.display.set_mode((431,768))

#game loop
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
    
    screen.blit(bg,(0,0))
    
    #run floor
    x_floor -= 1
    screen.blit(floor,(x_floor,0+600))
    pygame.display.update()