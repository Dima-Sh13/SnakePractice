import pygame as pg
from utils import * 
from Clases import Tank, Ammo

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("T.N.K")
tank = Tank()
game = True
while game:
   
    for evento in pg.event.get():
        if evento.type == pg.QUIT:  
            game = False          

    screen.fill(BLANCO)
    tank.draw(screen)
    tank.move()
    tank.shoot()
    mun = Ammo(tank.pos_x, tank.pos_y)
    mun.shot()
    
    pg.display.flip()


pg.quit()











