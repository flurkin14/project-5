import turtle
screen=turtle.Screen()
jim=turtle.Turtle()
jim.color("blue")
bob = turtle.Turtle()
bob.speed(50)
bob.pensize("3")
jim.pensize("3")
def pattern():
  
  for i in range(36):
    square()
    jim.right(10)
def circle():
  bob.circle(100)
def loop():
  counter=0
  while(counter<=36):
    circle()
    bob.right(10)
    counter+=1
    
  pattern()

def square():
  jim.forward(100)
  jim.right(90)
    


screen.onkey(loop,"s")
screen.listen()
