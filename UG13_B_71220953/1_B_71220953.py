import turtle

s = turtle.Screen()

t = turtle.Turtle()

t.penup()
t.goto(-200,0)
t.pendown()

#Y
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(180)
t.forward(100)
t.right(45)
t.forward(100)

#9
t.penup()
t.goto(0,0)
t.pendown()
t.right(45)
t.circle(-50)
t.penup()
t.goto(50,-50)
t.pendown()
t.right(90)
t.forward(80)
t.circle(-50,180)

#5
t.penup()
t.goto(100,0)
t.pendown()
t.right(90)
t.forward(60)
t.penup()
t.goto(100,0)
t.pendown()
t.right(90)
t.forward(60)
t.right(-90)
t.circle(-55,185)

#3
t.penup()
t.goto(200,0)
t.pendown()
t.right(180)
t.circle(-45,180)
t.right(160)
t.circle(-45,225)

#C
t.penup()
t.goto(360,-180)
t.pendown()
t.left(35)
t.circle(-90,180)

s.exitonclick()