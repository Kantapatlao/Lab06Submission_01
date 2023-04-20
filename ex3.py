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
class InputBox:

    def __init__(self, x, y, w, h, hoo ,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.int = hoo
    
    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
        
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if self.int == True:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                    else :

                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(450,250,30,30) # สร้าง Object จากคลาส Button ขึ้นมา

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)


input_box1 = InputBox(100, 100, 140, 32, False) # สร้าง InputBox1
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('NICK NAME', True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
textRect = text.get_rect() # text size
textRect.center = (115, 80)

input_box2 = InputBox(400, 100, 140, 32 , False) # สร้าง InputBox2
text2 = font.render('NAME', True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
textRect2 = text2.get_rect() # text size
textRect2.center = (415, 80)

input_box3 = InputBox(100, 300, 140, 32 , True) # สร้าง InputBox2
text3 = font.render('AGE', True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
textRect3 = text3.get_rect() # text size
textRect3.center = (115, 280)

input_boxes = [input_box1, input_box2 , input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
text4 = font.render('', True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
textRect4= text4.get_rect() # text size
textRect4.center = (115, 400)
while run:
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        r = 128
        g = 128
        b = 128
        if btn.isMousePressed():
            r = 255
            g = 0
            b = 255
            # box1 = (input_box1.text).strip
            # box2 = (input_box2.text).strip
            # box3 = (input_box3.text).strip
            box1 = input_box1.text
            box2 = input_box2.text
            box3 = input_box3.text
            if box1 == '' or box2 == '' or box3 == '': #box1 != '' or box2 != '' or box3 != ''
                FORRETURN = "PU TANG INA MO,BOBO KA"
                text4 = font.render(FORRETURN, True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
                textRect4= text4.get_rect() # text size
                textRect4.center = (int(win_x//2), 400)

            # elif box1.strip != '' or box2.strip != '' or box3.strip != '':
            else:
                FORRETURN = 'Hello ' + input_box1.text + input_box2.text + '! You are ' + input_box3.text + ' years old.'
                text4 = font.render(FORRETURN, True, pg.Color("BLACK"),None) # (text,is smooth?,letter color,background color)(0,0,0)
                textRect4= text4.get_rect() # text size
                textRect4.center = (int(win_x//2), 400)
        
    else:
        r = 255
        g = 0
        b = 0
        btn.w = 100
        btn.h = 100
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    btn.draw(screen)
    pg.time.delay(1)
    pg.display.update()
            
