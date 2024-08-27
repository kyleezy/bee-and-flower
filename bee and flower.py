import pgzrun
import random
WIDTH=700
HEIGHT=600
TITLE="bee game"
bee=Actor("bee")
bee.pos=(50,50)
flower=Actor("flower")
flower.pos=(350,300)
score=0
def draw():
    screen.clear()
    screen.blit("green.png",(0,0))
    screen.draw.text(str(score),(50,50))
    bee.draw()
    flower.draw()
def update():
    global score
    if keyboard.left:
        bee.x=bee.x-5
    if keyboard.right:
        bee.x=bee.x+5
    if keyboard.up:
        bee.y=bee.y-5
    if keyboard.down:
        bee.y=bee.y+5
    if bee.colliderect(flower):
        score=score+5
        x=random.randint(50,650)
        y=random.randint(50,550)
        flower.pos=x,y


 

   
   
   
   
   
   


pgzrun.go()