from turtle import *
from random import randint
speed(0)
for step in range(10):
   write(step+1)
   penup()
   right(90)
   forward(20)
   
   for breaks in range(10):
     pendown()
     forward(5)
     penup()
     forward(5)
     
   penup()
   backward(120)
   left(90)
   forward(20)
ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-30,-40)
ada.right(360)
ada.pendown()

bob=Turtle()
bob.color('green')
bob.shape('turtle')
bob.penup()
bob.goto(-30,-60)
bob.right(360)
bob.pendown()


boby=Turtle()
boby.color('yellow')
boby.shape('turtle')
boby.penup()
boby.goto(-30,-80)
boby.right(360)
boby.pendown()

aday=Turtle()
aday.color('orange')
aday.shape('turtle')
aday.penup()
aday.goto(-30,-100)
aday.right(360)
aday.pendown()

for turn in range(70):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  aday.forward(randint(1,5))
  boby.forward(randint(1,5))
