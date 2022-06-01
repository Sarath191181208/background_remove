import pygame 
from tkinter import colorchooser,Tk
class ColourButton():
    def __init__(self,colour,x,y,win) -> None:
        self.colour = colour
        self.win = win
        self.x,self.y =  x,y
        self.width,self.height = 20,20
        self.clicked = False

    def draw(self):
        stroke = 3
        pygame.draw.rect(self.win, (0,0,0), pygame.Rect(self.x-stroke, self.y-stroke, self.width+(2*stroke), self.height+(2*stroke)))
        pygame.draw.rect(self.win, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

    def is_hovering(self):
        threshold = 5
        return  (
            pygame.mouse.get_pos()[0] > self.x   -threshold     and 
            pygame.mouse.get_pos()[0] < self.x +self.width   +threshold     and
            pygame.mouse.get_pos()[1] > self.y  -threshold      and 
            pygame.mouse.get_pos()[1] < self.y +self.height +threshold      )

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.is_hovering():
            self.clicked = True
            root  = Tk()
            root.withdraw()
            color_code = colorchooser.askcolor(title ="Choose color")
            if color_code[0] is None:
                return
            print(color_code)
            self.colour = color_code[0]
        else:
            self.clicked = False
        self.draw()