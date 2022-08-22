import turtle as TK

t=TK.Turtle()

t.speed(100)
TK.bgcolor("black")

for i in range(240):
    t.color("cyan")
    t.circle(i)
    t.left(5)

TK.done()