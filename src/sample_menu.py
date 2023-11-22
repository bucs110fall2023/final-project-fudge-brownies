import pygame
from button import Button
pygame.init()

#screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Menu")

#button
resume_button = Button(304, 125, text="Resume")

#gamestates
game_paused = False

#Font
TEXT_COL = ('white')
font =  pygame.font.SysFont('arialblack',40)

#Text
def draw_text(text, font, text_col, x, y):
    img = font.render(text,True, text_col)
    screen.blit(img, (x,y))


#Gameloop
run = True
while run:
    screen.fill((52,78,91))

    #check if game is paused
    if game_paused == True:
        if resume_button.draw(screen):
            game_paused = False
    else:
        draw_text('Press Space to Pause', font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
            
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()