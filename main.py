import pygame as pg
from utils import * 
from Clases import Snake, Food




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

#Game Loop
while game:
    ts.tick(10)
    counter +=1
    screenGame.blit(fondo,(0,0))
   
    for evento in pg.event.get():
        if evento.type == pg.QUIT:  
            game = False          

   
    
    snake.draw(screenGame)
    snake.move()
    food.draw(screenGame)
    print(snake.pos_x, snake.pos_y)



    pg.display.flip()


pg.quit()











