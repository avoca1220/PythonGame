import os
import pygame as pg

CAPTION = "Test Program"
SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (40, 40, 40)
TRANSPARENT = (0, 0, 0, 0)


class Control(object):
    
    def __init__(self, UP, DOWN, LEFT, RIGHT):
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False
        
    def get_input(self):
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                if event.key == 273:
                    self.UP = True
                    self.DOWN, self.RIGHT, self.LEFT = False, False, False
                if event.key == 274:
                    self.DOWN = True
                    self.UP, self.RIGHT, self.LEFT = False, False, False
                if event.key == 275:
                    self.RIGHT = True
                    self.UP, self.DOWN, self.LEFT = False, False, False
                if event.key == 276:
                    self.LEFT = True
                    self.UP, self.DOWN, self.RIGHT = False, False, False
                    
            if event.type == pg.KEYUP:
                if event.key == 273:
                    self.UP = False
                if event.key == 274:
                    self.DOWN = False
                if event.key == 275:
                    self.RIGHT = False
                if event.key == 276:
                    self.LEFT = False
        


def main():
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    controls = Control(False, False, False, False)
    while True:
        controls.get_input()
        if controls.UP == True:
            print "UP"
        if controls.DOWN == True:
            print "DOWN"
        if controls.RIGHT == True:
            print "RIGHT"
        if controls.LEFT == True:
            print "LEFT"

main()
