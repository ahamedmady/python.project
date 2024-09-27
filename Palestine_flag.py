import turtle

#create window

screen = turtle.Screen()
screen.title("Free Palestine")
screen.bgcolor("gray")
screen.setup(width= 800, height= 600)

#create turtle to draw the flag

turtle_flag = turtle.Turtle()
turtle_flag.speed(5)
turtle_flag.hideturtle()
#Function to draw Rectangle
def Draw_rectangle(color,width,height):

    turtle_flag.begin_fill()
    turtle_flag.fillcolor(color)
    for _ in range(2):
        turtle_flag.forward(width)
        turtle_flag.left(90)
        turtle_flag.forward(height)
        turtle_flag.left(90)
    turtle_flag.end_fill()

#Draw the black strip
turtle_flag.penup()
turtle_flag.goto(-300,100)
turtle_flag.pendown()
Draw_rectangle("black",600,100)

#Draw the white strip
turtle_flag.penup()
turtle_flag.goto(-300,0)
turtle_flag.pendown()
Draw_rectangle("white",600,100)

#Draw the green strip
turtle_flag.penup()
turtle_flag.goto(-300,-100)
turtle_flag.pendown()
Draw_rectangle("green",600,100)

#Draw the red triangle 

turtle_flag.penup()
turtle_flag.goto(-300,200)
turtle_flag.pendown()
turtle_flag.begin_fill()
turtle_flag.fillcolor("red")
turtle_flag.goto(-100,50)
turtle_flag.goto(-300,-100)
turtle_flag.goto(-300,100)
turtle_flag.end_fill()

turtle.done()



