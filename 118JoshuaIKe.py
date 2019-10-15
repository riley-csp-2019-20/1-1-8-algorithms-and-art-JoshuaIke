import turtle as trtl
Remi= trtl.Turtle()
Remi.pensize(3)
Remi.speed(0)
Remi.pendown()
#this code is used for creating the main head of the mouse
Remi.pencolor("red")
count= 0
Remi.setheading(30)
while (count < 3):
 Remi.forward(100)
 Remi.right(120)
 count = count + 1
 #Now after creating the head you move on to making the mousers whiskers.
Remi.setheading(15)
Remi.pencolor("gray")
Remi.forward(60)
Remi.backward(60)
Remi.pencolor("red")
Remi.setheading(0)
Remi.pencolor("gray")
Remi.forward(70)
Remi.backward(70)
Remi.pencolor("red")
Remi.setheading(340)
Remi.pencolor("gray")
Remi.forward(50)
Remi.backward(50)
Remi.pencolor("red")
Remi.setheading(30)
Remi.forward(100)
#this code is useful to help create the mouses eye
Remi.penup()
Remi.goto(80,15)
Remi.pendown()
Remi.pencolor("black")
#This code is for the mouses pupil
Remi.fillcolor("yellow")
Remi.begin_fill()
Remi.circle(8)
Remi.end_fill()
 
 
Remi.circle(12)
Remi.penup()
#This is for the mouses main body.
Remi.goto(87,50)
Remi.setheading(270)
Remi.pencolor("dark blue")
Remi.pendown()
Remi.forward(100)
Remi.setheading(0)
Remi.forward(140)
Remi.penup()
Remi.goto(87,50)
Remi.pendown()
Remi.forward(140)
Remi.setheading(270)
Remi.forward(100)
Remi.penup()
#This code is for the mouse's ear
Remi.goto(87,60)
Remi.pencolor("light blue")
Remi.pendown()
Remi.circle(50)
Remi.penup()
#This code is for the mouses legs
Remi.goto(87,-50)
Remi.pencolor("black")
Remi.pendown()
#enter a number less then 20 for the code to work
num = int(input("Enter a number -> "))
if (num <= 20):
 Remi.forward(80)
 Remi.setheading(0)
 Remi.forward(30)
 Remi.setheading(90)
 Remi.forward(80)
else:
 Remi.forward(100)
 #Repeat step 71 for the other leg but change the location for the other leg
Remi.penup()
Remi.goto(190,-50)
Remi.pendown()
num = int(input("Enter a number -> "))
if (num <= 20):
 Remi.setheading(270)
 Remi.forward(80)
 Remi.setheading(0)
 Remi.forward(30)
 Remi.setheading(90)
 Remi.forward(80)
 #this is the code for the tail
 tail = 0
 while (tail < 2):
    Remi.penup()
    Remi.color("pink")
    Remi.goto(228,-5)
    Remi.setheading(320)
    Remi.pendown()
    Remi.forward(80)
    tail = tail + 1
#this is the code to make the tail animate
    tail_color = 0
    if (tail_color % 18 == 0):
        Remi.color("navy")

wn = trtl.Screen()
wn.mainloop()
 
