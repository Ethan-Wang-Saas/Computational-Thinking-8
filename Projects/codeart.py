import turtle 

#make john
john= turtle.Turtle()
john.penup()
john.goto(175,-10)
john.color("red")
john.pendown()
john.speed(10000)

#make jim
jim= turtle.Turtle()
jim.penup()
jim.goto(-235,-10)
jim.color("red")
jim.pendown()
jim.speed(10000)

#make billy
billy= turtle.Turtle()
billy.penup()
billy.goto(210,0)
billy.color("Orange")
billy.pendown()
billy.speed(10000)

#make t
t= turtle.Turtle()
t. penup()
t.goto(-200,0)
t.pendown()
t.speed(10000)


for i in range(500):
    t.forward(50+i)
    t.right(11+1)
    t.color("brown")
    t.forward(12+i)
    t.right(140+1)
    t.color("Orange")
    t.circle(2+i)
    t.color("green")
    t.forward(50+i)
    t.right(32+1)
    t.color("blue")
    t.circle(10)
    t.color("purple")

    billy.forward(50+i)
    billy.right(11+1)
    billy.color("brown")
    billy.forward(12+i)
    billy.right(140+1)
    billy.color("Orange")
    billy.circle(2+i)
    billy.begin_fill
    billy.forward(10)
    billy.end_fill
    billy.color("green")
    billy.forward(50+i)
    billy.right(32+1)
    billy.color("blue")
    billy.circle(10)
    billy.color("Purple")

    john.forward(100)
    john.left(191)

    jim.forward(100)
    jim.left(191)
turtle.exitonclick()



