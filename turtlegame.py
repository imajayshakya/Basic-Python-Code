from turtle import*
from random import*
title("Turtle  Rancing Game  Hosted by Laxmi Boys Hostel")
speed(10)
penup()
goto(-240,240)
z=0
y=25
pensize(10)
for x in range(6):
	write(x)
	right(90)
	forward(10)
	pendown()
	forward(50)
	penup()
	backward(160)
	left(90)
	forward(y)

t1=Turtle()
t1.penup()
t1.goto(-240,200)
t1.color("red")
t1.shape("turtle")

t2=Turtle()
t2.penup()
t2.goto(-240,150)
t2.color("black")
t2.shape("turtle")

t3=Turtle()
t3.penup()
t3.goto(-240,100)
t3.color("Green")
t3.shape("turtle")

for i in range(50):
	t1.forward(randint(1,40))
	t2.forward(randint(1,40))
	t3.forward(randint(1,40))