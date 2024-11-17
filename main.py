from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()
img = "india-political-map.gif"

screen.addshape(img)
screen.setup(height=950, width=800)
turtle.shape(img)

def get_coordinates(x,y):
    print(f"Coordinated x: {x}, y: {y}")


screen.mainloop()