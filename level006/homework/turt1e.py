from turtle import*

# setup
speed(10)
width(3)
screensize(800,600)
# castle side 1
fillcolor("grey")
begin_fill()
forward(400)   

left(90)
forward(300)
left(90)
forward(25)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(100)
# middle part only castles no doors yet



right(90)
forward(25)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)



left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

# skekleton of one side done

# start of second side]

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)

left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)



right(90)
forward(100)
left(90)
forward(25)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(300)
# lines 
left(90)
forward(125)
left(90)
forward(300)
left(180)
forward(300)
left(90)
forward(525)
left(90)
forward(300)
left(180)
forward(300)
right(90)
forward(200)
end_fill()
# door
fillcolor("chocolate4")
begin_fill()
right(90)
forward(50)


# door circle

circle(40, 180)

left(0)
forward(50)
end_fill()
left(90)
forward(40)
left(90)
forward(90)
left(180)
forward(90)
right(90)
forward(350)
right(90)

# window 1
fillcolor("black")
begin_fill()
penup()
goto(-310, 150)
pendown()
right(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
end_fill()
# window 2
fillcolor("black")
begin_fill()
penup()
goto(340, 190)
pendown()
right(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)

end_fill()


# flags
penup()
goto(-310, 300)
pendown()
fillcolor("green")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
end_fill()
# txt goa 
penup()
goto(-350, 330)
pendown()

write("GOA", font=("Arial", 10, "bold"))
left(90)
# flag 2
penup()
goto(340, 300)
pendown()
fillcolor("green")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
end_fill()
# txt goa 
penup()
goto(350, 330)
pendown()

write("GOA", font=("Arial", 10, "bold"))

# sky
bgcolor("skyblue")


# grass
penup()
goto(-600, -1)
pendown()
color("green")
begin_fill()
right(180)
forward(1600)
right(90)
forward(400)
right(90)
forward(1600)

end_fill()


#sun
penup()
goto(200, 500)
pendown()
color("yellow")
begin_fill()
circle(100)
end_fill()





















# end <3






