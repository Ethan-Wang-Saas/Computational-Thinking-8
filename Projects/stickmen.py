import turtle

# Create a turtle object
pen = turtle.Turtle()
pen.speed(10)  

# stickmen place
def draw_stickman(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Head
    pen.circle(50)

    # Body
    pen.penup()
    pen.goto(x, y - 0)
    pen.pendown()
    pen.goto(x, y - 100)

    # Left arm
    pen.penup()
    pen.goto(x, y - 50)
    pen.pendown()
    pen.goto(x - 40, y - 70)

    # Right arm
    pen.penup()
    pen.goto(x, y - 50)
    pen.pendown()
    pen.goto(x + 40, y - 70)

    # Left leg
    pen.penup()
    pen.goto(x, y - 100)
    pen.pendown()
    pen.goto(x - 30, y - 150)

    # Right leg
    pen.penup()
    pen.goto(x, y - 100)
    pen.pendown()
    pen.goto(x + 30, y - 150)

# Draw two stickmen at different positions
draw_stickman(-100, 100)  # Stickman 1
draw_stickman(100, 100)   # Stickman 2

# Hide the turtle
pen.hideturtle()

# Finish the drawing
turtle.done()
