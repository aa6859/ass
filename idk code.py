def visualize(lines):
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pencolor('red')
    t.pd()
    for i in range(0,len(lines)):
        for p in lines[i]:
            t.goto(p[0]*640/1024-320,-(p[1]*640/1024-320))
            t.pencolor('black')
        t.pencolor('red')
    turtle.mainloop()