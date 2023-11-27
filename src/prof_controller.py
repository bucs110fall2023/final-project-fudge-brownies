import pygame
from button import Button


TEXT_COL = ('white')

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode() #work on sizing and work on button layout
    WIDTH, HEIGHT = self.screen.get_size()
    pygame.display.set_caption("Fourier Draw")
    #menu buttons go there
    self.color = "red"
    self.resume_button = Button((WIDTH/2 - 87.5), 125, color=(105,105,105), text="Resume")
    self.options_button = Button((WIDTH/2 - 87.5), 250, color=(105,105,105), text="Options")
    self.quit_button = Button((WIDTH/2 - 87.5), 375, color=(105,105,105), text="Quit")
    self.color_button = Button((WIDTH/2 - 87.5), 125, color=(105,105,105), text="Color")
    self.equation_button = Button((WIDTH/2 - 87.5), 250, color=(105,105,105), text="Equation")
    self.back_button = Button((WIDTH/2 - 87.5), 375, color=(105,105,105), text="Back")
    self.back_button2 = Button((WIDTH/2 - 87.5), 375, color=(105,105,105), text="Back")
    

    self.buttons = pygame.group.Group(self.resume_button, self.options_button, self.quit_button, 
                                      self.color_button, self.equation_button, self.back_button, self.back_button2
                                      )
    #gamestates
    self.game_paused = False
    self.menu_state = 'Paused'
    self.font =  pygame.font.SysFont('arialblack',10)

    def draw_text(self, text, font, text_col, x, y):
      img = font.render(text,True, text_col)
      self.screen.blit(img, (x,y))
    
  def mainloop(self):
    #select state loop
    while True:
      if self.state == 'Menu':
         self.menuloop()
    
      elif self.state == 'Gameloop':
         self.gameloop()

      elif self.state == 'Options':
        self.optionsloop()
    
      elif self.state == 'Color':
        self.colorloop()
    
      elif self.state == 'Equation':
        self.equationloop()

    
  
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
              self.state == 'Options'
      # not update section

      # need to redraw buttons
      self.buttons.draw(self.screen)
      
      pygame.display.update()
        
  def optionsloop(self):
    while self.state == 'Options':
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
          if self.color_button.rect.collidepoint(event.pos):
                self.state == "Color"
          if self.equation_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state == 'Equation'
          if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state == 'Menu'
      # not update section

      # need to redraw buttons
      self.buttons.draw(self.screen)
      
      pygame.display.update()
  
  def colorloop(self):
    while self.state == 'Color':
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
          if self.color_button.rect.collidepoint(event.pos): #make these a bunch of colors
                pass
          
          if self.back_button2.rect.collidepoint(pygame.mouse.get_pos()):
              self.state == 'Options'
      # not update section

      # need to redraw buttons
      self.buttons.draw(self.screen)
      
      pygame.display.update()
       
     

               
      
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
