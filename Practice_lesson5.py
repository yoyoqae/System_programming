import turtle

turtle.Turtle()
pen = turtle.Pen()
screen = turtle.Screen()
pen.pensize(3)
pen.speed(0)

screen.bgcolor("skyblue")

#трава
pen.penup()
pen.goto(-500, -150)
pen.pendown()
pen.pencolor("green")
pen.begin_fill()
for i in range(2):
    pen.forward(1000)
    pen.right(90)
    pen.forward(250)
    pen.right(90)
pen.color("green")
pen.end_fill()

#дом
pen.penup()
pen.goto(-100, -147)
pen.pendown()
pen.color("orange")
pen.pensize(3)
pen.begin_fill()
for i in range(4):
    pen.forward(170)
    pen.left(90)
pen.end_fill()


#крыша
pen.penup()
pen.goto(-127,25)
pen.pendown()
pen.color("brown")
pen.begin_fill()
for i in range(3):
    pen.forward(225)
    pen.left(120)
pen.end_fill()

#окно
pen.penup()
pen.goto(0,-50)
pen.pendown()
pen.color("skyblue")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

#крестовина на окне (горизонтально)
pen.penup()
pen.goto(0,-25)
pen.pendown()
pen.color("black")
pen.forward(50)

#вертикально
pen.penup()
pen.goto(25,-50)
pen.pendown()
pen.color("black")
pen.left(90)
pen.forward(50)

#дверь
pen.penup()
pen.goto(-80,-147)
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

#окно на крыше
pen.penup()
pen.goto(-50,50)
pen.pendown()
pen.color("skyblue")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

#крестовина на окне (горизонтально)
pen.penup()
pen.goto(-50,75)
pen.pendown()
pen.color("black")
pen.forward(50)

#вертикально
pen.penup()
pen.goto(-25, 50)
pen.pendown()
pen.color("black")
pen.left(90)
pen.forward(50)

#Ромашка
pen.penup()
pen.goto(190, -145)
pen.setheading(90)
pen.pendown()

# Стебель
pen.color("green")
pen.width(4)
pen.forward(70)

# Центр цветка (белый круг)
pen.penup()
pen.goto(202, -63)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Лепестки
pen.penup()
pen.goto(270, -63)
pen.pendown()
pen.color("yellow")
pen.width(6)

for angle in range(0, 360, 45):
    pen.penup()
    pen.goto(190, -63)
    pen.setheading(angle)
    pen.pendown()
    pen.forward(25)


pen.penup()
pen.goto(200,200)
pen.color("black")
pen.write("дом моей мечты")
turtle.done()