from turtle import*


#we want to paint a house

#step 1: draw a square
width(7)
speed(10)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing windows

penup()
goto(15,180)
pendown()
color("brown")
left(30)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)

#drawing second window

penup()
goto(185,180)
pendown()
color("brown")
forward(40)
left(90)
forward(60)
left(90)
forward(39)
left(90)
forward(60)



exitonclick()



