import pygame
from src.controller_class import Controller
from src.button import Button

def main():
    pygame.init()
    #Create an instance on your controller object
    controller_instance = Controller()
    #Call your mainloop
    controller_instance.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

