import turtle
import random
from turtle import Turtle,Screen
tortoise=Turtle()
screen=Screen()
tortoise.pensize(10)
tortoise.speed("fast")
colors=["red","green","blue","brown","black","pink","yellow","violet","purple"]
def spirograph(): 
    n=int(input("Enter a number: "))
    for i in range(n):
        tortoise.color(random.choice(colors))
        tortoise.circle(100)
        tortoise.left(10)
    screen.exitonclick()
while(True):
    choice=input("Do you want to continue drawing the spirograph: ")
    if(choice=="yes"):
        spirograph()
    else:
        print("Thank you for using our application!")
        break