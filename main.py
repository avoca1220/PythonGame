import os
import pygame as pg

CAPTION = "Test Program"
SCREEN_SIZE = (1420, 800)
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
        self.grid = [1, 8]
        self.xpos = 80
        self.ypos = 80
        self.input_control = input_control

        self.hrz_speed_base = 2
        self.vrt_speed_base = 2

    def move(self):
        
        if self.input_control.UP == True:
            self.ypos -= self.vrt_speed_base
            if self.ypos <= (720-(80 * self.grid[1])):
                self.grid[1] += 1

        if self.input_control.DOWN == True:
            self.ypos += self.vrt_speed_base
            if self.ypos > (800-(80 * self.grid[1])):
                self.grid[1] -= 1
            
        if self.input_control.LEFT == True:
            self.xpos -= self.hrz_speed_base
            if self.xpos < (80 * self.grid[0]):
                self.grid[0] -= 1
            
        if self.input_control.RIGHT == True:
            self.xpos += self.hrz_speed_base
            if self.xpos > (80 * self.grid[0]) + 80:
                self.grid[0] += 1
            
'''
0-79 = 9
80-159 = 8
160-239 = 7
240-319 = 6
320-399 = 5
400-479 = 4
480-559 = 3
560-639 = 2
640 719 = 1
720-800 = 0
'''


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
        pg.draw.rect(screen, (100, 100, 100), pg.Rect(player.xpos, player.ypos, 80, 160))
        pg.display.flip()

        print "Current grid is " + str(player.grid)
        
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
