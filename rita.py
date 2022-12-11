import turtle as tu

tu.Screen().bgcolor("black")

t = tu.Turtle()
t.pensize(3)
t.speed(0)

t.pencolor("red")

for i in range(62):
    t.left(59)
    t.forward(150)
    t.circle(88)
    t.backward(75)
    t.circle(44)
    t.backward(75)

tu.done()