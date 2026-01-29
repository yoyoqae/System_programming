import turtle

turtle.Turtle()
pen = turtle.Pen()
screen = turtle.Screen()
pen.pensize(7)

turtle.shape("turtle")

#трава
screen.bgcolor("green")

#небо
pen.penup()
pen.goto(-400,-100)
pen.pendown()
pen.color("skyblue")
pen.begin_fill()
for i in range(2):
    pen.forward(800)
    pen.left(90)
    pen.forward(500)
    pen.left(90)
pen.end_fill()

#дом
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.color("white")
pen.pensize(3)
pen.begin_fill()
for i in range(4):
    pen.forward(170)
    pen.left(90)
pen.end_fill()


#крыша
pen.penup()
pen.goto(-127,70)
pen.pendown()
pen.color("black")
pen.begin_fill()
for i in range(3):
    pen.forward(225)
    pen.left(120)
pen.end_fill()

#окно
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.color("skyblue")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

#крестовина на окне (горизонтально)
pen.penup()
pen.goto(0,25)
pen.pendown()
pen.color("black")
pen.forward(50)

#вертикально
pen.penup()
pen.goto(25,0)
pen.pendown()
pen.color("black")
pen.left(90)
pen.forward(50)

#дверь
pen.penup()
pen.goto(-70,-90)
pen.pendown()
pen.right(90)
pen.color("brown")
pen.begin_fill()
for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

#окно
pen.penup()
pen.goto(-50,100)
pen.pendown()
pen.color("skyblue")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

#крестовина на окне (горизонтально)
pen.penup()
pen.goto(-50,125)
pen.pendown()
pen.color("black")
pen.forward(50)

#вертикально
pen.penup()
pen.goto(-25, 100)
pen.pendown()
pen.color("black")
pen.left(90)
pen.forward(50)

pen.penup()
pen.goto(200,200)
pen.color("black")
pen.write("дом моей мечты")
turtle.done()