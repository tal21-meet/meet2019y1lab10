import turtle
bullet=turtle.clone()
bullet.hideturtle()
bad_guy_pos =(100,0)
good_pos =(0,0)
def shot ():
    bullet.penup()
    bullet.goto(good_pos)
    bullet.showturtle()
    bullet_pos=bullet.pos()
    bullet_xpos=b
    while bullet_pos==bad_guy_pos or bullet_xpos >= 100 or bullet_xpos <= -100 :
        bullet.forward(1)
        bullet_pos=bullet.pos()

if bullet_xpos >= 100 or bullet_xpos <= -100:
    bullet.hideturtle()
else:
    score += 1
    bullet.hideturtle()
