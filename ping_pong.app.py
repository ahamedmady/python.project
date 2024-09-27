"""['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator',
 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', 
 '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__forwardmethods', '__func_body', '__loader__', '__methodDict', '__methods', '__name__', '__package__', '__spec__', '__stringBody',
 '_alias_list', '_make_global_funcs', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities',
   '_turtle_docrevise', '_ver', 'addshape', 'back', 'backward'dict', 'deepcopy',
 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward',
   'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 
   'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left',
   'listen', 'lt', 'mainloop', 'math', 'mode', 'numinput',
 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown',
   'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 
   'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos',  
 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 
 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 
'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 
'up', 'update', 'warnings', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']"""
#imported module tertule

import turtle

# print(dir(turtle))

screen = turtle.Screen()#create window 

screen.title("ping pong by 'Mohamed' ")#set the title of the window

screen.bgcolor("black")#set the undergroundcolor of window

screen.setup(width=800, height=600)#create width and height of window

screen.tracer(0)#ste not update of window

#madrap1
madrap1= turtle.Turtle()
madrap1.speed(0)
madrap1.shape("square")
madrap1.shapesize(stretch_wid=5, stretch_len= 1)
madrap1.color("red")
madrap1.penup()
madrap1.goto(-380,0)

#madrap2
madrap2= turtle.Turtle()
madrap2.speed(0)
madrap2.shape("square")
madrap2.shapesize(stretch_wid=5, stretch_len= 1)
madrap2.color("blue")
madrap2.penup()
madrap2.goto(370,0)
# #ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.2
ball.dy = 0.2

#score 
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Plary1 : 0 , Plary2 : 0", align= "center",font=("courier",20,"normal"))

#function to move Up
def madrap1_up():
     y = madrap1.ycor()
     y +=20
     madrap1.sety(y)

def madrap1_Dwon():
     y = madrap1.ycor()
     y -=20
     madrap1.sety(y)

#keyword binding

screen.listen()
screen.onkeypress(madrap1_up, "w")
screen.onkeypress(madrap1_Dwon, "s")


#function to move Up
def madrap2_up():
     y = madrap2.ycor()
     y +=20
     madrap2.sety(y)

def madrap2_Dwon():
     y = madrap2.ycor()
     y -=20
     madrap2.sety(y)


#keyword binding

screen.listen()
screen.onkeypress(madrap2_up, "Up")
screen.onkeypress(madrap2_Dwon, "Down")

while True:
     screen.update()
     # move the ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)

     #border chack 

     if ball.ycor() > 290:
          ball.sety(290)
          ball.dy *= -1

     elif ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1

     
     elif ball.xcor() > 390:
         ball.goto(0,0)
         ball.dx *= -1
         score2 += 1
         score.clear()
         score.write(f"Plary1 : {score1} , Plary2 : {score2}", align= "center",font=("courier",24,"normal"))
         
     elif ball.xcor() < -390:
         ball.goto(0,0)
         ball.dx *= -1
         score1 += 1
         score.clear()
         score.write(f"Plary1 : {score1} , Plary2 : {score2}", align= "center",font=("courier",24,"normal"))

     if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < madrap2.ycor() + 40 and ball.ycor() > madrap2.ycor() - 40 ):
          
          ball.setx(360)
          ball.dx *= -1



     if (ball.xcor() < -370 and ball.xcor() > -380) and (ball.ycor() < madrap1.ycor() + 40 and ball.ycor() > madrap1.ycor() - 40 ):
          
          ball.setx(-370)
          ball.dx *= -1

