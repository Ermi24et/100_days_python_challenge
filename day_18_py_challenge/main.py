import turtle as t
import random

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def hirst_painting(grid_size=10, dot_size=20, dot_gap=50):

    my_t = t.Turtle()
    t.colormode(255)

    # Set initial position of turtle
    screen_size_x = t.window_width()
    screen_size_y = t.window_height()
    my_t.pu()
    my_t.setpos(-screen_size_x/4, -screen_size_y/4)

    # Draw dots
    for _ in range(grid_size):
        start_x = my_t.xcor()
        start_y = my_t.ycor()

        for _ in range(grid_size):
            my_t.dot(dot_size, random.choice(color_list))
            my_t.pu()
            my_t.fd(dot_gap)

        my_t.pu()
        my_t.goto(start_x, start_y + 50)

    screen = t.Screen()
    screen.exitonclick()


hirst_painting()