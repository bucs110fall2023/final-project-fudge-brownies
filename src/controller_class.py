import pygame
from src.button import Button


TEXT_COL = ('white')

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode() #work on sizing and work on button layout
    self.WIDTH, self.HEIGHT = self.screen.get_size()
    pygame.display.set_caption("Fourier Draw")
    #menu buttons go there
    self.resume_button = Button((self.WIDTH/2 - 87.5), ((self.HEIGHT/3)/2 - 37.5), color=(105,105,105), text="Resume")
    self.options_button = Button((self.WIDTH/2 - 87.5), ((self.HEIGHT/3 + self.HEIGHT/3/2)-37.5), color=(105,105,105), text="Options")
    self.quit_button = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Quit")
    self.color_button = Button(self.WIDTH/2 - 87.5, (self.HEIGHT/3)/2 - 37.5, color=(105,105,105), text="Color")
    #self.equation_button = Button(self.WIDTH/2 - 87.5, (self.HEIGHT/3 + self.HEIGHT/3/2)-37.5, color=(105,105,105), text="Equation")

    self.back_button = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")
    #self.back_button2 = Button((self.WIDTH/2 - 87.5), 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")
    self.back_button2 = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")

    #color buttons
    self.color = (255,0,0)
    self.red_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(255,0,0), text="R")
    self.blue_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(0,0,255), text="Bl")
    self.green_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(2,207,2), text="G")
    self.yellow_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(255,255,0), text="Y")
    self.orange_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(255,128,0), text="O")
    self.purple_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(127,0,255), text="Pu")
    self.pink_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(255,153,255), text="Pi")
    self.gold_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(219, 172, 52), text="Au")
    self.silver_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(192,192,192), text="Ag")

    self.menu_buttons = pygame.sprite.Group(self.resume_button, self.options_button, self.quit_button)
    
    self.options_buttons = pygame.sprite.Group(self.color_button, self.back_button)
    
    self.color_buttons = pygame.sprite.Group(self.back_button2, self.red_button, self.blue_button, self.green_button, self.yellow_button,
                                      self.orange_button, self.purple_button, self.pink_button, self.gold_button, self.silver_button)
    
    
    #gamestates
    #self.game_paused = False #ask if redudant
    #self.menu_state = 'Paused' #ask if redudant
    self.state = 'Gameloop'
    self.font =  pygame.font.SysFont('arialblack',30)

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
    
      #elif self.state == 'Equation':
        #self.equationloop()

    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    while self.state == 'Menu':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.menu_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.resume_button.rect.collidepoint(event.pos):
                self.state = "Gameloop"
          if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
              pygame.quit()
          if self.options_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Options'
      # not update section

      # need to redraw buttons
      self.menu_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      
      pygame.display.update()
        
  def optionsloop(self):
    while self.state == 'Options':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.options_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.color_button.rect.collidepoint(event.pos):
                self.state = "Color"
          #if self.equation_button.rect.collidepoint(pygame.mouse.get_pos()):
              #self.state == 'Equation'
          if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Menu'
      # not update section

      # need to redraw buttons
      self.options_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      
      pygame.display.update()
  
  def colorloop(self):
    while self.state == 'Color':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.color_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.red_button.rect.collidepoint(event.pos): 
                self.color = (255,0,0)
                print('red')
          if self.green_button.rect.collidepoint(event.pos): 
                self.color = (0,255,0)
                print('green')
          if self.blue_button.rect.collidepoint(event.pos): 
                self.color = (2,207,2)
                print('blue')
          if self.yellow_button.rect.collidepoint(event.pos):
                self.color = (255,255,0)
                print('yellow')
          if self.orange_button.rect.collidepoint(event.pos): 
                self.color = (255,128,0)
                print('orange')
          if self.purple_button.rect.collidepoint(event.pos): 
                self.color = (127,0,255)
                print('purple')
          if self.pink_button.rect.collidepoint(event.pos): 
                self.color = (255,153,255)
                print('pink')
          if self.gold_button.rect.collidepoint(event.pos): 
                self.color = (219, 172, 52)
                print('gold')
          if self.silver_button.rect.collidepoint(event.pos): 
                self.color = (192,192,192)
                print('silver')
          
          if self.back_button2.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Options'
      # not update section

      # need to redraw buttons
      self.color_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      self.draw_text("Choose your Color!", self.font, TEXT_COL, self.WIDTH/2 - 87.5, (self.HEIGHT/3 + self.HEIGHT/3/2)-37.5+30)
      
      pygame.display.update()
       
     

               
      
  def gameloop(self):
    while self.state == 'Gameloop':
      self.screen.fill((0,0,0))
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  self.state = "Menu"
              if event.key == pygame.K_ESCAPE:
                  pygame.quit()

              
          if event.type == pygame.QUIT:  
              run = False

      if self.state != 'Gameloop':
            break
      
      self.draw_text("Press ESC to Exit, Press Space for Menu", self.font, TEXT_COL, 20, 20)
      pygame.display.update()
    

###################################

#Text



#Gameloop




#def test():
#   c = Controller()
#   c.mainloop()

#if "__name__" == __main__:
#   test()