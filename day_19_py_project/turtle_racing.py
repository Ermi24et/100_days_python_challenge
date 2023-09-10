from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_guess = screen.textinput("put your bet", "which turtle wins: choose color")
print(user_guess)
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
x_cord = -288
y_cord = [-220, -130, -40, 50, 140, 230]
turtle_list = []
race_on = False
for i in range(len(colors)):
    turtle_racers = Turtle()
    turtle_racers.shape("turtle")
    turtle_racers.color(colors[i])
    turtle_racers.penup()
    turtle_racers.goto(x=x_cord, y=y_cord[i])
    turtle_list.append(turtle_racers)
if user_guess:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 280:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you won the game..! the {winning_color} color is tyhe winner..!")
            else:
                print(f"you lost the game..the {winning_color} color is the winner..!")
        distance = random.randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()