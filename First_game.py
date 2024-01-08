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

#game object bird
bird = pygame.image.load(r'FileGame\assets\yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)

bird_rectangle = bird.get_rect(center=(100,768/2))

#trọng lực P
P = 0.1
y_bird = 0


#game loop
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                y_bird = -10   
    
    screen.blit(bg,(0,0))
    
    #run floor
    x_floor -= 1
    screen.blit(floor,(x_floor,0+600))
    screen.blit(floor,(x_floor + 432,0+600))
    if(x_floor <= -432):
        x_floor = 0
        
    #add bird in game
    screen.blit(bird,bird_rectangle) 
    y_bird += P
    bird_rectangle.centery += y_bird   
        
    pygame.display.update()