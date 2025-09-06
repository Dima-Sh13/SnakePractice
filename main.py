import pygame as pg
from utils import * 
from Clases import Snake, Food, Boton
from random import randint




#Initial conf of pygame
pg.init()
screenGame = pg.display.set_mode((W, H))
pg.display.set_caption("Sssnake")
ts = pg.time.Clock()
fondo = pg.image.load("grass.png")
fondo = pg.transform.scale(fondo, (W,H))
snake = Snake()
game = True
counter = 0
food = Food()
fruit = Boton((randint(0,W),randint(0,H)))

#Game Loop
while game:
    ts.tick(10)
    fruit_on = True
    screenGame.blit(fondo,(0,0))
    counter += 10
    for evento in pg.event.get():
        if evento.type == pg.QUIT:  
            game = False          

   
    
    snake.draw(screenGame)
    snake.move()
    #food.draw(screenGame)
    if (snake.pos_x >= fruit.pos_chx[0] and snake.pos_x <= fruit.pos_chx[1]) and (snake.pos_y>= fruit.pos_chy[0] and snake.pos_y <= fruit.pos_chy[1]):
        fruit_on = False
        
        
    if fruit_on == True:
        ruit = Boton((randint(0,W),randint(0,H)))
        fruit.show(screenGame)
    print(snake.pos_x, snake.pos_y,fruit.pos_chx, fruit.pos_chy, counter)




    pg.display.flip()


pg.quit()











