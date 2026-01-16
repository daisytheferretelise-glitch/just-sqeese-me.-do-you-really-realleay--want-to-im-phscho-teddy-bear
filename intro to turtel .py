import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(400,500)

polygon=turtle.Turtle()
num_sides=10
side_lenght=100
angle= 360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()