import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
pen.penup()
pen.goto(-300,300)
pen.pendown()

figures.draw_triangle(pen, 100)

pen.penup()
pen.goto(300,300)
pen.pendown()

figures.draw_triangle(pen, 100)

pen.penup()
pen.goto(200,-200)
pen.pendown()

figures.draw_rectangle(pen, 100, 200)

pen.penup()
pen.goto(-200,-200)
pen.pendown()

figures.draw_rectangle(pen, 100, 200)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
