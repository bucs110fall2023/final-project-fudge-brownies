import pygame
from button import Button



class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fourier Draw")
    #menu buttons go there
    self.resume_button = Button(304, 125, color=(105,105,105), text="Resume")
    self.options_button = Button(304, 250, color=(105,105,105), text="Options")
    self.quit_button = Button(304, 375, color=(105,105,105), text="Quit")
    self.color_button = Button(304, 125, color=(105,105,105), text="Color")
    self.equation_button = Button(304, 250, color=(105,105,105), text="Equation")
    self.back_button = Button(304, 375, color=(105,105,105), text="Back")

    #self.state = 'Menu'
    #self.state = 'Options'
    
  def mainloop(self):
    #select state loop
    if self.state == 'Menu':
       self.menuloop()
    
    elif self.state == 'Gameloop':
       self.gameloop()

    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    
    while self.state == 'Menu':
   
      for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

        if events.type == pygame.MOUSEBUTTONDOWN:

          if self.start_button.collidepoint(events.pos):
                self.state == "Gameloop"

          
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  
