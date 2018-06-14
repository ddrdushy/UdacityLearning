import turtle

def drawSquare(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()

    brad.shape("circle")
    brad.color("white","gray")
    brad.speed(2)

    for i in range(1,37):
        drawSquare(brad)
        brad.right(10)

    window.exitonclick()

drawArt()