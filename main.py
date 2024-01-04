from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("SkyBlue")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for _ in range(3):
#     timmy.pencolor("blue")
#     timmy.left(60)
#     timmy.backward(100)
#     timmy.left(180)
#
# for _ in range(4):
#     timmy.pencolor("black")
#     timmy.right(90)
#     timmy.forward(100)
#
# for _ in range(5):
#     timmy.pencolor("pink")
#     timmy.right(72)
#     timmy.forward(100)
#
# for _ in range(6):
#     timmy.pencolor("green")
#     timmy.right(60)
#     timmy.forward(100)
#
# for _ in range(7):
#     timmy.pencolor("green")
#     timmy.right(54)
#     timmy.forward(100)

colors = ["red", "blue", "green", "yellow", "pink"]
# def draw(num_of_sides):
#     angle = 360/num_of_sides
#     for _ in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for num_of_sides in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw(num_of_sides)

# timmy.pensize(10)
# timmy.speed("fastest")
color = ("blue", "red", "skyblue", "orange", "purple", "black", "green")
direction = (0, 90, 180, 270)
# while True:
#     timmy.color(random.choice(color))
#     timmy.right(random.choice(direction))
#     timmy.forward(random.choice(range(0, 100)))
#     timmy.left(random.choice(direction))
#     timmy.backward(random.choice(range(0, 100)))
#
#


def random_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    tup = (r, g, b)
    return tup


# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

timmy.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading()+10)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
