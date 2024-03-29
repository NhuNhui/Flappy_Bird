# add library pygame
import pygame
pygame.init ()

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
P = 0.05
y_bird = 0

game_play = True
#score
score = 0
max_score = 0

game_font = pygame.font.Font(r'FileGame\04B_19.TTF',40)
def display_score():
    if(game_play):
        score_font = game_font.render(f"SCORE: {str(score)}",True,(255,255,255))
        score_rect = score_font.get_rect(center=(432/2,100))
        screen.blit(score_font,score_rect)
        
        # max_score_font = game_font.render(f"HIGH SCORE: {str(max_score)}",True,(255,255,255))
        # max_score_rect = max_score_font.get_rect(center=(432/2,60))
        # screen.blit(max_score_font,max_score_rect)
    else:
        
        score_font = game_font.render(f"SCORE: {str(score)}",True,(255,255,255))
        score_rect = score_font.get_rect(center=(432/2,100))
        screen.blit(score_font,score_rect)
        
        max_score_font = game_font.render(f"HIGH SCORE: {str(max_score)}",True,(255,255,255))
        max_score_rect = max_score_font.get_rect(center=(432/2,60))
        screen.blit(max_score_font,max_score_rect)

#func check var
game_play = True
def check_var() -> bool:
    if(bird_rectangle.bottom >= 768 - 100 or bird_rectangle.top <= 0):
        return False
    return True

#game_over
game_over = pygame.image.load(r'FileGame\assets\message.png')
game_over = pygame.transform.scale2x(game_over)
game_over_rectangle = game_over.get_rect(center=(432/2,768/2))

   

#game loop
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE and game_play):
                y_bird = -3 
                score += 1
                
            if(event.key == pygame.K_SPACE and game_play == False):
                game_play = True
                y_bird = 0
                bird_rectangle.center=(100,768/2)
                score = 0
    
    screen.blit(bg,(0,0))
    
    #run floor
    x_floor -= 1
    screen.blit(floor,(x_floor,0+600))
    screen.blit(floor,(x_floor + 432,0+600))
    if(x_floor <= -432):
        x_floor = 0
        
    if game_play:
        #add bird in game
        screen.blit(bird,bird_rectangle) 
        y_bird += P
        bird_rectangle.centery += y_bird   
        display_score()
        game_play = check_var()
    else:
        screen.blit(game_over,game_over_rectangle)
        if(score > max_score):
            max_score = score
        display_score()
    
    pygame.display.update()