import pygame
from button import Button



class Controller:
  
  def __init__(self):
    #setup pygame data
    self.start_button = Button(text='Start')
    self.quit_button = Button(text = 'Quit')
    self.
    #menu buttons go there
    self.state = 'Menu'
    self.state = 'Gameloop'
    
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

          elif pbutton.collidepoint(events.pos):
                darts()
                #function purple
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  
