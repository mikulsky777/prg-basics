import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

figures.draw_square(100)

pen.hideturtle()
window.mainloop()