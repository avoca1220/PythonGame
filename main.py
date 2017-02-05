import os
import pygame as pg

CAPTION = "Test Program"
SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (40, 40, 40)
TRANSPARENT = (0, 0, 0, 0)

clock = pg.time.Clock()

class Grid(object):
    '''
    The game's grid, controling which blocks may be walked through and which may not
    '''
    def __init__(self):
        self.array = []

    def load_raw(self, width, height):
        self.width = width
        self.height = height
        for x_it in range(self.width):
            self.array.append([])
            
            for y_it in range(self.height):
                self.array[x_it].append([0])
        
            



class Control(object):
    
    def __init__(self):
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False
        self.SPACE = False
        
    def get_input(self):
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                if event.key == 273:
                    self.UP = True

                if event.key == 274:
                    self.DOWN = True

                if event.key == 275:
                    self.RIGHT = True

                if event.key == 276:
                    self.LEFT = True

                if event.key == 32:
                    self.SPACE = True

                    
            if event.type == pg.KEYUP:
                if event.key == 273:
                    self.UP = False
                    
                if event.key == 274:
                    self.DOWN = False
                    
                if event.key == 275:
                    self.RIGHT = False
                    
                if event.key == 276:
                    self.LEFT = False

                if event.key == 32:
                    self.SPACE = False

class Player(object):
    def __init__(self, input_control):
        self.xpos = 50
        self.ypos = 50
        self.input_control = input_control

    def move(self):
        
        if self.input_control.UP == True:
            self.ypos -= 0.5
            
        if self.input_control.DOWN == True:
            self.ypos += 0.5
            
        if self.input_control.LEFT == True:
            self.xpos -= 0.5
            
        if self.input_control.RIGHT == True:
            self.xpos += 0.5
            

def main():
    clock.tick(60)
    pg.init()
    pg.display.set_caption(CAPTION)
    screen = pg.display.set_mode(SCREEN_SIZE)
    controls = Control()
    #Player gets input through 'controls'
    player = Player(controls)
    grid = Grid()
    grid.load_raw(50, 10)

    for x_it in range(grid.width):
        grid.array[x_it][2] = 1

        print grid.array[x_it]
        
    while True:

        screen.fill((0, 0, 0))
        controls.get_input()
        player.move()
        pg.draw.rect(screen, (100, 100, 100), pg.Rect(player.xpos, player.ypos, 80, 80))
        pg.display.flip()
        
        if controls.UP == True:
            pass
            #print "UP"
        if controls.DOWN == True:
            pass
            #print "DOWN"
        if controls.RIGHT == True:
            pass
            #print "RIGHT"
        if controls.LEFT == True:
            pass
            #print "LEFT"
        

main()
