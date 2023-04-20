import sys 
import pygame as pg
r = 255
g = 0
b = 0
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))
class Button(Rectangle) :
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if(mouseX >= self.x and mouseY >= self.y and mouseX <= self.x+self.w and mouseY <= self.y+self.h):
            return True
        else :
            return False
    def isMousePressed(self):
        if(pg.mouse.get_pressed()[0]):
            return True
        else :
            return False
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(10,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        r = 128
        g = 128
        b = 128
        btn.w = 200
        btn.h = 300
        if btn.isMousePressed():
            r = 255
            g = 0
            b = 255
    else:
        r = 255
        g = 0
        b = 0
        btn.w = 100
        btn.h = 100
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
            