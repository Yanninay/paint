from turtle import *
from random import choice

paint = Turtle()
paint.color("black")
paint.width(10)
paint.shape('circle')
paint.pendown()
paint.speed(10)
def drawing(one, two): paint.goto(one, two)
print("Добро пожаловать в Paint! Доступные команды:")
print("Цвета:\ng - green (Зелёный), r - red (Красный), b - blue (Синий), l - lavender (Цвет лаванды), y - yellow (Жёлтый), i - lime (Лаймовый), w - white (белый), a - black (чёрный), s - skyblue (Светло-синий), e - grey (серый)")
print("Кнопки:\nстрелка вверх - вперёд на 5 пикселей, стрелка вниз - вниз на 5 пикселей, стрелка влево - влево на 5 пикс, стрелка вправо - вправо на 5 пикс")
print("Старт заполнения - t, заполнить - f")
def moving(x, y):
    paint.penup()
    paint.goto(x, y)
    paint.pendown()

screen = paint.getscreen()
screen.listen()

class Width: 
    def __init__(self, n): 
        self.n = n 
        self.n_l = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
 
    def change(self): 
        if self.n in self.n_l: 
            paint.width(self.n_l.index(self.n)+1) 
 
for i in range(1, 10): 
    screen.onkey(Width(str(i)).change, i)

# colors
def Green():
    paint.color('green')
screen.onkey(Green, 'g')
def Red():
    paint.color('red')
screen.onkey(Red, 'r')
def Blue():
    paint.color('blue')
screen.onkey(Blue, 'b')
def Lavander():
    paint.color('lavender')
screen.onkey(Lavander, 'l')
def Yellow():
    paint.color('yellow')
screen.onkey(Yellow, 'y')
def Lime():
    paint.color('lime')
screen.onkey(Lime, 'i')
def White():
    paint.color('white')
screen.onkey(White, 'w')
def Black():
    paint.color('black')
screen.onkey(Black, 'a')
def Skyblue():
    paint.color('skyblue')
screen.onkey(Skyblue, 's')
def Viollete():
    paint.color('violet')
screen.onkey(Viollete, 'v')
def Grey():
    paint.color('grey')
screen.onkey(Grey, 'e')
def cls():
    paint.clear()
    paint.penup()
    paint.goto(0,0)
    paint.pendown()
screen.onkey(cls, 'c')
def home():
    paint.penup()
    paint.goto(-120, 0)
    paint.pendown()
    paint.color("grey")
    for i in range(50):
        paint.goto(paint.xcor() + 5, paint.ycor())
    paint.left(90)
    for i in range(40):
        paint.goto(paint.xcor(), paint.ycor() + 5)
    paint.right(90)
    for i in range(50):
        paint.goto(paint.xcor() - 5, paint.ycor())
    paint.left(90)
    for i in range(40):
        paint.goto(paint.xcor(), paint.ycor() - 5)
    paint.right(55)
    paint.forward(10)
    paint.begin_fill()
    paint.color("sliver")
    for i in range(50):
        paint.goto(paint.xcor() + 5, paint.ycor())
    paint.left(90)
    for i in range(40):
        paint.goto(paint.xcor(), paint.ycor() + 5)
    paint.right(90)
    for i in range(50):
        paint.goto(paint.xcor() - 5, paint.ycor())
    paint.left(90)
    for i in range(40):
        paint.goto(paint.xcor(), paint.ycor() - 5)
    paint.end_fill()
    # COMPUTER
    paint.color("skyblue")
    paint.penup()
    paint.goto(-40,150)
    paint.pendown()
    paint.right(125)
    paint.forward(75)
    paint.right(90)
    paint.forward(95)
    paint.right(90)
    paint.forward(75)
    paint.right(90)
    paint.forward(95)
    # LOGO WINDOWS
    paint.color("grey")
    paint.penup()
    paint.goto(-10,100)
    paint.pendown()
    paint.begin_fill()
    paint.forward(20)
    paint.right(90)
    paint.forward(20)
    paint.right(90)
    paint.forward(20)
    paint.right(90)
    paint.forward(20)
    paint.end_fill()
    # NOSHKA
    paint.color("grey")
    paint.penup()
    paint.goto(-50,0)
    paint.pendown()
    paint.begin_fill()
    paint.left(90)
    paint.forward(100)
    paint.left(90)
    paint.forward(100)
    paint.left(90)
    paint.forward(100)
    paint.end_fill()
    

screen.onkey(home, 'h')

# keys
def Right():
    paint.goto(paint.xcor() + 5, paint.ycor())
def Left():
    paint.goto(paint.xcor() - 5, paint.ycor())
def Up():
    paint.goto(paint.xcor(), paint.ycor() + 5)
def Down():
    paint.goto(paint.xcor(), paint.ycor() - 5)
def Start_fill():
    paint.begin_fill()
def end_fill():
    paint.end_fill()

screen.onkey(Right, 'Right')
screen.onkey(Left, 'Left')
screen.onkey(Up, 'Up')
screen.onkey(Down, 'Down')
screen.onkey(Start_fill, 't')
screen.onkey(end_fill, 'f')
screen.onscreenclick(moving)
paint.ondrag(drawing)
