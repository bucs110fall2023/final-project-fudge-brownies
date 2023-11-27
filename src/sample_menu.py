import pygame
from button import Button
pygame.init()

#screen
screen = pygame.display.set_mode((800,600))#play with sizes
pygame.display.set_caption("Fourier Draw")

#button
resume_button = Button(304, 125, color=(105,105,105), text="Resume")
options_button = Button(304, 250, color=(105,105,105), text="Options")
quit_button = Button(304, 375, color=(105,105,105), text="Quit")
color_button = Button(304, 125, color=(105,105,105), text="Color")
equation_button = Button(304, 250, color=(105,105,105), text="Equation")
back_button = Button(304, 375, color=(105,105,105), text="Back")

#color buttons
red_button = Button(100, 125, width=75, height=75,  color=(255,0,0), text="Red")
blue_button = Button(100, 250, width=75, height=75,  color=(0,0,255), text="Blue")
green_button = Button(100, 375, width=75, height=75,  color=(0,255,0), text="Green")

#gamestates
game_paused = False
menu_state = 'Paused'


#Font
TEXT_COL = ('white')
font =  pygame.font.SysFont('arialblack',10)

#Text
def draw_text(text, font, text_col, x, y):
    img = font.render(text,True, text_col)
    screen.blit(img, (x,y))


#Gameloop
run = True
while run:
    screen.fill((52,78,91))

    a,b = pygame.mouse.get_pos()

    #check if game is paused
    if game_paused == True:
            if menu_state == 'Paused':
                resume_button.color_default()
                screen.blit(resume_button.image, resume_button.rect.topleft)
                if resume_button.rect.x <= a <= resume_button.rect.x +175 and resume_button.rect.y <= b <= resume_button.rect.y +75:
                    resume_button.highlight()
                    screen.blit(resume_button.image, resume_button.rect.topleft)
            
                options_button.color_default()
                screen.blit(options_button.image, options_button.rect.topleft)
                if options_button.rect.x <= a <= options_button.rect.x +175 and options_button.rect.y <= b <= options_button.rect.y +75:
                     options_button.highlight()
                     screen.blit(options_button.image, options_button.rect.topleft)
            
                quit_button.color_default()
                screen.blit(quit_button.image, quit_button.rect.topleft)
                if quit_button.rect.x <= a <= quit_button.rect.x +175 and quit_button.rect.y <= b <= quit_button.rect.y +75:
                     quit_button.highlight()
                     screen.blit(quit_button.image, quit_button.rect.topleft)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if resume_button.rect.collidepoint(pygame.mouse.get_pos()):
                            game_paused = False
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if options_button.rect.collidepoint(pygame.mouse.get_pos()):
                            menu_state = 'Options'
            
            if menu_state == 'Options':
                color_button.color_default()
                screen.blit(color_button.image, color_button.rect.topleft)
                if color_button.rect.x <= a <= color_button.rect.x +175 and color_button.rect.y <= b <= color_button.rect.y +75:
                    color_button.highlight()
                    screen.blit(color_button.image, color_button.rect.topleft)
            
                equation_button.color_default()
                screen.blit(equation_button.image, equation_button.rect.topleft)
                if equation_button.rect.x <= a <= equation_button.rect.x +175 and equation_button.rect.y <= b <= equation_button.rect.y +75:
                     equation_button.highlight()
                     screen.blit(equation_button.image, equation_button.rect.topleft)
            
                back_button.color_default()
                screen.blit(back_button.image, back_button.rect.topleft)
                if back_button.rect.x <= a <= back_button.rect.x +175 and back_button.rect.y <= b <= back_button.rect.y +75:
                     back_button.highlight()
                     screen.blit(back_button.image, back_button.rect.topleft)
                #colors
                red_button.color_default()
                screen.blit(red_button.image, red_button.rect.topleft)
                if red_button.rect.x <= a <= red_button.rect.x +75 and red_button.rect.y <= b <= red_button.rect.y +75:
                    red_button.highlight()
                    screen.blit(red_button.image, red_button.rect.topleft)
            
                blue_button.color_default()
                screen.blit(blue_button.image, blue_button.rect.topleft)
                if blue_button.rect.x <= a <= blue_button.rect.x +75 and blue_button.rect.y <= b <= blue_button.rect.y +75:
                     blue_button.highlight()
                     screen.blit(blue_button.image, blue_button.rect.topleft)
            
                green_button.color_default()
                screen.blit(green_button.image, green_button.rect.topleft)
                if green_button.rect.x <= a <= green_button.rect.x +75 and green_button.rect.y <= b <= green_button.rect.y +75:
                     green_button.highlight()
                     screen.blit(green_button.image, green_button.rect.topleft)               

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if color_button.rect.collidepoint(pygame.mouse.get_pos()):
                            pass
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if equation_button.rect.collidepoint(pygame.mouse.get_pos()):
                            pass
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                            menu_state = 'Paused'
            
                    

    else:
        draw_text('Press Space for Menu', font, TEXT_COL, 20, 20)

        

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
            
        if event.type == pygame.QUIT:  #ask how to make x button work in all menus
            run = False
    
    pygame.display.update()

pygame.quit()