import pygame as pg
from utils import *
from random import randint

class Snake():
    def __init__(self):
        self.hp = 1
        self.ammo = 50
        self.pos_x_i = W//2
        self.pos_y_i = H//2
        self.vy = 0
        self.vx = 0
        self.pos_x =  W -self.pos_x_i 
        self.pos_y = H - self.pos_y_i
        
        

    def draw(self,screen):
        pg.draw.rect(screen,NEGRO, (self.pos_x, self.pos_y, 50,50))

    def move(self):
        
        teclas = pg.key.get_pressed()  
        self.pos_x += self.vx
        self.pos_y += self.vy
        
        if teclas[pg.K_UP] and self.pos_y >= 0:  
            self.vy = -10
            self.vx = 0
        if teclas[pg.K_DOWN] and self.pos_y < H - h_tank: 
            self.vy = 10
            self.vx = 0
            if self.pos_y > H -h_tank:
                self.vy = 0
        if teclas[pg.K_LEFT] and self.pos_x >= 0:   
            self.vx = -10
            self.vy = 0
        if teclas[pg.K_RIGHT] and self.pos_x <= W - w_tank: 
            self.vx = 10
            self.vy = 0
        #Loop to create infinite scenario
        if self.pos_y < 0:
            self.pos_y = H -self.pos_y
        elif self.pos_y > H:
            self.pos_y = self.pos_y - H    

        if self.pos_x < 0:
            self.pos_x = W - self.pos_x   
        elif self.pos_x > W:
            self.pos_x = self.pos_x - W


    
class Food():
    def __init__(self):
        self.pos_x = randint(0, W)
        self.pos_y = randint(0, H)
        self.vx = 1
        self.vy = 1
        
    def draw(self,screen):
        pg.draw.rect(screen,NEGRO, (self.pos_x, self.pos_y, 20,20))

               