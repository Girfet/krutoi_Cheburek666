import turtle 
import time

turtle.shape("turtle")

turtle.color("green")
turtle.pencolor("red")
turtle.speed(10)
# a = 0
# while a != 4:
#   turtle.forward(100)
#   turtle.right(90)
#   a += 1



# a = 5

# while a <= 145:
#   turtle.forward(a)
#   turtle.right(60)
#   a += 5
  
# turtle.pencolor("blue")
# turtle.right(60)
# turtle.forward(10)
# turtle.right(60)
# a -= 15

# while a >= 10:
#   turtle.forward(a)
#   turtle.left(60)
#   a -= 5
# for i in range(4):
#   turtle.forward(100)
#   turtle.right(90)
# turtle.pencolor('blue')

# for i in range(6):
#   turtle.forward(75)
#   turtle.right(60)
# turtle.pencolor('green')

# for i in range(3):
#   turtle.forward(100)
#   turtle.right(120)

# s = int(input('стороны: '))
# a = int(input('длина 1 строны: '))
# for i in range(s):
#   turtle.forward(a)
#   turtle.right(360 / s)

a = 10
for i in range(20):
  for i in range(12):
    turtle.forward(a)
    turtle.right(30)
  a += 10


turtle.mainloop()
