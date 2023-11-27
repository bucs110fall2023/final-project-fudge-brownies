import pygame
from button import Button


TEXT_COL = ('white')

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fourier Draw")
    #menu buttons go there
    self.color = "red"
    self.resume_button = Button(304, 125, color=(105,105,105), text="Resume")
    self.options_button = Button(304, 250, color=(105,105,105), text="Options")
    self.quit_button = Button(304, 375, color=(105,105,105), text="Quit")
    self.color_button = Button(304, 125, color=(105,105,105), text="Color")
    self.equation_button = Button(304, 250, color=(105,105,105), text="Equation")
    self.back_button = Button(304, 375, color=(105,105,105), text="Back")
    self.buttons = pygame.group.Group(self.resume_button, self.options_button, self.quit_button, self.color_button, self.equation_button, self.back_button)
    #gamestates
    self.game_paused = False
    self.menu_state = 'Paused'
    self.font =  pygame.font.SysFont('arialblack',10)

    def draw_text(self, text, font, text_col, x, y):
      img = font.render(text,True, text_col)
      self.screen.blit(img, (x,y))
    
  def mainloop(self):
    #select state loop
    if self.state == 'Menu':
       self.menuloop()
    
    elif self.state == 'Gameloop':
       self.gameloop()
    elif self.state == 'Options':
      self.optionsloop()

    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    while self.state == 'Menu':
      self.screen.fill((52,78,91))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONMOVE:
          for button in self.buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.resume_button.rect.collidepoint(event.pos):
                self.state == "Gameloop"
          if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
              pygame.quit()
          if self.options_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Options'
      # not update section

      # need to redraw buttons
      self.buttons.draw(self.screen)
      
      pygame.display.update()
        
def optionsloop(self):
    while self.state == 'Options':
      # color_button.color_default()
      # screen.blit(color_button.image, color_button.rect.topleft)
      # if color_button.rect.x <= a <= color_button.rect.x +175 and color_button.rect.y <= b <= color_button.rect.y +75:
      #     color_button.highlight()
      #     screen.blit(color_button.image, color_button.rect.topleft)
  
      # equation_button.color_default()
      # screen.blit(equation_button.image, equation_button.rect.topleft)
      # if equation_button.rect.x <= a <= equation_button.rect.x +175 and equation_button.rect.y <= b <= equation_button.rect.y +75:
      #     equation_button.highlight()
      #     screen.blit(equation_button.image, equation_button.rect.topleft)
  
      # self.back_button.color_default()
      # screen.blit(self.back_button.image, self.back_button.rect.topleft)
      # if self.back_button.rect.x <= a <= self.back_button.rect.x +175 and self.back_button.rect.y <= b <= self.back_button.rect.y +75:
      #     self.back_button.highlight()
      #     screen.blit(self.back_button.image
      # pygame.quit(), self.back_button.rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if color_button.rect.collidepoint(pygame.mouse.get_pos()):
                    pass
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if equation_button.rect.collidepoint(pygame.mouse.get_pos()):
                    pass
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_state = 'Paused'              
                      

      else:
          self.draw_text('Press Space for Menu',self.font, TEXT_COL, 20, 20)

          
      
  def gameloop(self):

      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  self.state = "Menu"
              
          if event.type == pygame.QUIT:  #ask how to make x button work in all menus
              run = False
      
      pygame.display.update()
    
  

###################################

#Text



#Gameloop
